# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from importlib import import_module
from voluptuous import Optional
import os
import re

from taskgraph.parameters import extend_parameters_schema
from mozilla_taskgraph import register as mozilla_taskgraph_register

from . import branch_builds
from .build_config import get_version_from_version_txt

PREVIEW_RE = re.compile(r'\[preview ([\w-]+)\]')
def register(graph_config):
    # Import modules to register decorated functions
    _import_modules([
        "actions.release_promotion",
        "branch_builds",
        "job",
        "target_tasks",
        "transforms",
        "worker_types",
    ])

    extend_parameters_schema({
        Optional('branch-build'): {
            Optional('firefox-android-owner'): str,
            Optional('firefox-android-branch'): str,
        },
        # Publish a "preview build" for a future version.  This is set to
        # "nightly" for the nightly builds.  Other strings indicate making a
        # preview build for a particular application-services branch.
        'preview-build': Optional(str),
        # Release type.  Set to `release` or `nightly` when we're building release artifacts.
        'release-type': Optional(str),
    })

    # Register mozilla-taskgraph extensions
    mozilla_taskgraph_register(graph_config)


def _import_modules(modules):
    for module in modules:
        import_module(f".{module}", package=__name__)

def get_decision_parameters(graph_config, parameters):
    if parameters["tasks_for"] == "github-release":
        head_tag = parameters["head_tag"]
        if not head_tag:
            raise ValueError(
                "Cannot run github-release if `head_tag` is not defined. Got {}".format(
                    head_tag
                )
            )
        version = get_version_from_version_txt()
        # XXX: tags are in the format of `v<semver>`
        if head_tag[1:] != version:
            raise ValueError(
                "Cannot run github-release if tag {} is different than in-tree "
                "{version} from buildconfig.yml".format(head_tag[1:], version)
            )
        parameters["target_tasks_method"] = "full"
    elif parameters["tasks_for"] == "github-pull-request":
        pr_title = os.environ.get("APPSERVICES_PULL_REQUEST_TITLE", "")
        preview_match = PREVIEW_RE.search(pr_title)
        if preview_match is not None:
            if preview_match.group(1) == 'nightly':
                parameters["preview-build"] = "nightly"
                parameters["target_tasks_method"] = "full"
            elif preview_match.group(1) == 'release':
                parameters["target_tasks_method"] = "full"
                parameters["release-type"] = "release"
            else:
                raise NotImplemented("Only nightly preview builds are currently supported")
        elif "[ci full]" in pr_title:
            parameters["target_tasks_method"] = "pr-full"
        elif "[ci skip]" in pr_title:
            parameters["target_tasks_method"] = "pr-skip"
        else:
            parameters["target_tasks_method"] = "pr-normal"
    elif parameters["tasks_for"] == "github-push":
        if parameters["head_tag"].startswith("release-"):
            parameters["target_tasks_method"] = "release"
            parameters["release-type"] = "release"
    elif parameters["tasks_for"] == "cron":
        # We don't have a great way of determining if something is a nightly or
        # not.  But for now, we can assume all cron-based builds are nightlies.
        parameters["preview-build"] = "nightly"
        parameters["release-type"] = "nightly"

    parameters['branch-build'] = branch_builds.calc_branch_build_param(parameters)
    parameters['filters'].extend([
        'branch-build',
    ])

    parameters["existing_tasks"] = {
        "Build summary task": "DUv85m5GRz--vq2aKUT3Ig",
        "build-docker-image-linux": "BX4oKRwHTumeMA6Gf3ximA",
        "fetch-go-1.14.4": "a_m7s0hcS0y5Jcjtk-r7aQ",
        "fetch-resource-monitor": "Xkamopv9S1a49ZGkDzygLw",
        "fetch-swiftformat": "WkWxWdYgTnipA0axTg4Paw",
        "lint-detekt": "W87QvU0MRPGgbNtNrBJ-9A",
        "lint-ktlint": "bc3QlFghTxmVDNMUT1tFzg",
        "module-build-autofill": "asovqHjbT96tLokYpTopVg",
        "module-build-crashtest": "EMQcZSCTQ06eQMOzDqKpZA",
        "module-build-errorsupport": "PJngxpqdTpqRYVISrnYvaA",
        "module-build-full-megazord": "UpnaUeByThup1MeVwPmt2w",
        "module-build-fxaclient": "MOrotkiVQzWaoROoKNRb_w",
        "module-build-httpconfig": "B8FsRpoJQIK_WyfQx4GrJg",
        "module-build-logins": "dxnF1wkwQxiDfjWw9WtIHQ",
        "module-build-native-support": "Gy3w3LF7SOeLBzvN3MQ0Iw",
        "module-build-nimbus": "VtlRpNXNRlu6fs0jXqyv-Q",
        "module-build-places": "eVrnif6VRoKa0e3Y35qzjg",
        "module-build-push": "Pci0WWcHTfmhutbiK9Jy1w",
        "module-build-remotesettings": "OnvBH-5VTRqqvp-43dx0Rw",
        "module-build-rust-log-forwarder": "HfAVrnQiQfm8hc-_L2f8gw",
        "module-build-rustlog": "FFHv9gK2QKmn6z6QF3FaRA",
        "module-build-suggest": "KS7h8-SgSO2lBYOyJPMBMA",
        "module-build-sync15": "AxyNeFrJQ6yJujR89cJ8pw",
        "module-build-syncmanager": "a5HpI5bjTxGTHiDepUxGmA",
        "module-build-tabs": "FzMHjY7OQOiMH1nD-0C2WA",
        "module-build-tooling-nimbus-gradle": "UiFrWFpBT_qPRcgxWGOwfA",
        "nimbus-binaries-assemble-nimbus-cli": "O60patY-TheH-bOWN118BQ",
        "nimbus-binaries-assemble-nimbus-fml": "VBiOfR8WQ6yEim2alqfuPQ",
        "nimbus-build-cli-linux": "Tue2CQgSREe-SGvk4xKImg",
        "nimbus-build-cli-osx-aarch64": "MpCQZcIsSlK8p_MD6tZFiw",
        "nimbus-build-cli-osx-x86-64": "NFlegADLRTu098jL-yylAQ",
        "nimbus-build-cli-windows": "QHO-3cZNSQyI_NoGfHOckQ",
        "nimbus-build-fml-linux": "b1xCT9lPSKObsU6-C2n4zA",
        "nimbus-build-fml-osx-aarch64": "AddmUgEgTFmQFWZjHBdlNQ",
        "nimbus-build-fml-osx-x86-64": "PqLQZ4kLTwaj4MraDzZlKw",
        "nimbus-build-fml-windows": "N_QmMn-xSuSIBTduD7jW8A",
        "swift-build": "Gs1LNMByQcydA3mO8XxCRw",
        "toolchain-android": "OsOSTthDQHyVbPk85RK_Ig",
        "toolchain-desktop-linux": "eI4-1314QcSA3NtwoQPXqQ",
        "toolchain-desktop-macos": "EfEhlwDGS-aq6_5zsMpF_g",
        "toolchain-libs-ios": "IVZYUwg-Q9CWiAB-PDMWVw",
        "toolchain-linux64-resource-monitor": "J2wudsdqQzq06fkB-t0wJA",
        "toolchain-macosx64-resource-monitor": "VWghkn7kR4eeuazL1z49HA",
        "toolchain-robolectric": "Tjcmx4yCQMmVhJ-ReRlYmg",
        "toolchain-rust": "boiFQLowSFa6UvS_W9fPdA",
        "toolchain-rust-osx": "FD0jD4tkT6Oj9lTbZtYK8A"
    }
