searchState.loadedDescShard("rc_crypto", 0, "Contains the error value\nContains the success value\nThis crate provides all the cryptographic primitives …\nOnly required to be called if you intend to use this …\nReturns the argument unchanged.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nAES-128 in GCM mode with 128-bit tags and 96 bit nonces.\nAES-256 in GCM mode with 128-bit tags and 96 bit nonces.\nThe additional authenticated data (AAD) for an opening or …\nAES-256 in CBC mode with HMAC-SHA256 tags and 128 bit …\nThe nonce for an opening or sealing operation. This is a …\nThe key’s AEAD algorithm.\nThe key’s AEAD algorithm.\nConstruct an empty <code>Aad</code>.\nReturns the argument unchanged.\nConstruct the <code>Aad</code> by borrowing a contiguous sequence of …\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nThe length of the key.\nCreate a new opening key.\nCreate a new sealing key.\nThe length of the nonces.\nThe length of a tag.\nA key agreement algorithm.\nThe key may be used at most once.\nThe result of a key agreement operation, to be fed into a …\nA key pair for key agreement.\nHow many times the key may be used.\nA private key for key agreement.\nA public key for key agreement.\nThe key may be used more than once.\nAn unparsed public key for key agreement.\nThe whole point of having <code>Ephemeral</code> and <code>Static</code> lifetimes …\nEphemeral agreement. This consumes <code>self</code>, ensuring that the …\nStatic agreement. This borrows <code>self</code>, allowing the private …\nCalls <code>kdf</code> with the raw key material and then returns what …\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nGenerate a new key pair for the given algorithm.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nThe private key.\nThe public key.\nSplit the key pair apart.\nReturns <code>Ok(())</code> if <code>a == b</code> and <code>Error</code> otherwise. The …\nVerify that the signature matches the input data.\nA calculated digest value.\nReturns the digest of data using the given digest …\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nReturns the argument unchanged.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nA calculated signature value. This is a type-safe wrappper …\nA key to use for HMAC signing.\nA key to use for HMAC authentication.\nReturns the argument unchanged.\nReturns the argument unchanged.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.\nCalculate the HMAC of <code>data</code> using <code>key</code>.\nCalculate the HMAC of <code>data</code> using <code>key</code> and verify it …\nEquivalent to <code>verify</code> but allows the consumer to pass a …\nExtend passwords using pbkdf2, based on the following rfc …\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nFill a buffer with cryptographically secure pseudo-random …\nAn unparsed public key for signature operations.\nA signature verification algorithm.\nReturns the argument unchanged.\nReturns the argument unchanged.\nCalls <code>U::from(self)</code>.\nCalls <code>U::from(self)</code>.")