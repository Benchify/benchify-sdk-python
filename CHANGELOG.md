# Changelog

## 0.8.0 (2026-02-25)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/Benchify/benchify-sdk-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** api update ([f17bb88](https://github.com/Benchify/benchify-sdk-python/commit/f17bb881929a54d56e181167942b29966e6239e1))
* **api:** api update ([988433a](https://github.com/Benchify/benchify-sdk-python/commit/988433adb17c6723785fcc79d112d1235864858e))
* **api:** api update ([acbdbdd](https://github.com/Benchify/benchify-sdk-python/commit/acbdbddbfc8a6bf0c32339b4a68635500cf7bb73))
* **api:** api update ([3a56790](https://github.com/Benchify/benchify-sdk-python/commit/3a56790797c67b357047e2cf3ffcc857490e28ea))
* **api:** api update ([b42ea01](https://github.com/Benchify/benchify-sdk-python/commit/b42ea01495e0b0b68712d3845933a1fd16964e1c))
* **api:** api update ([db0f873](https://github.com/Benchify/benchify-sdk-python/commit/db0f87365147f7478889d69bf6e14807a878c30a))
* **api:** manual updates ([c3106c7](https://github.com/Benchify/benchify-sdk-python/commit/c3106c7a605a7dc8711ca81f96863a5e20ae81be))
* **api:** manual updates ([4e28d49](https://github.com/Benchify/benchify-sdk-python/commit/4e28d49d08c13027bf89b728d8139bf6f8a8e1d4))
* **api:** manual updates ([9d3bc91](https://github.com/Benchify/benchify-sdk-python/commit/9d3bc91b39de22ee755e7afb125665ac7d62d7c7))
* **api:** manual updates ([86d3bcd](https://github.com/Benchify/benchify-sdk-python/commit/86d3bcd4b43249e2a7e86723184968be5ac435ae))
* **api:** manual updates ([676a40a](https://github.com/Benchify/benchify-sdk-python/commit/676a40a70134370ecdca261c9804bbe8939e8d9b))
* **client:** add custom JSON encoder for extended type support ([11383dd](https://github.com/Benchify/benchify-sdk-python/commit/11383dd4f5806a594f3131f423c4e27c150e3200))
* **client:** add support for binary request streaming ([2c35482](https://github.com/Benchify/benchify-sdk-python/commit/2c35482f9d7fc168d95dc23b7eff85503739b369))


### Bug Fixes

* **client:** loosen auth header validation ([8c22a38](https://github.com/Benchify/benchify-sdk-python/commit/8c22a38c0969909e0aa24b5a856b59a6f506ba9b))
* compat with Python 3.14 ([75b948d](https://github.com/Benchify/benchify-sdk-python/commit/75b948d1aa8d9bc26eef28b9a71e39ba8b9b2c9a))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([096f67b](https://github.com/Benchify/benchify-sdk-python/commit/096f67bad9d1d7f8e55987ec4a1a15e3a41f224a))
* **docs:** fix mcp installation instructions for remote servers ([378d782](https://github.com/Benchify/benchify-sdk-python/commit/378d7822f3073a570ddbf64f4a4521a210f0fdf9))
* ensure streams are always closed ([04ce4dc](https://github.com/Benchify/benchify-sdk-python/commit/04ce4dc454aab185e59aec577c12eb89252045f7))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([fae18b6](https://github.com/Benchify/benchify-sdk-python/commit/fae18b6333d3697845bbf233ea20f55c96202561))
* use async_to_httpx_files in patch method ([7732f70](https://github.com/Benchify/benchify-sdk-python/commit/7732f705f48dd431880c8ed65708a4cf5b8eff06))


### Chores

* add missing docstrings ([2564e8d](https://github.com/Benchify/benchify-sdk-python/commit/2564e8dbd691cd3ca3d47ed56dcdb21c96ef249f))
* add Python 3.14 classifier and testing ([dc5218c](https://github.com/Benchify/benchify-sdk-python/commit/dc5218cfd1712d7b2bf5671b2985ae12eae6d4b7))
* **ci:** upgrade `actions/github-script` ([b0d0279](https://github.com/Benchify/benchify-sdk-python/commit/b0d0279c1f1b22a6ff09802fb1d04dd66dd1c0a4))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([69a5933](https://github.com/Benchify/benchify-sdk-python/commit/69a5933b2a0671dd5c4d8a50bfa15e0af49d0a9c))
* **docs:** use environment variables for authentication in code snippets ([0a45222](https://github.com/Benchify/benchify-sdk-python/commit/0a45222f9cbf46b0319c20b382c4d6bf593c148b))
* format all `api.md` files ([711513d](https://github.com/Benchify/benchify-sdk-python/commit/711513df3f25b7a222c6d6a98843c5a6d9fc1e9c))
* **internal:** add `--fix` argument to lint script ([3cfbbf7](https://github.com/Benchify/benchify-sdk-python/commit/3cfbbf79912010c381c10a4ec25c0b96eac0a5f9))
* **internal:** add missing files argument to base client ([d16ba69](https://github.com/Benchify/benchify-sdk-python/commit/d16ba6962962dd2feb5c5d5d9ef6d102f9f6c576))
* **internal:** add request options to SSE classes ([354018a](https://github.com/Benchify/benchify-sdk-python/commit/354018a24317362a1b089ecfc05cb054bf50fe98))
* **internal:** bump dependencies ([6681cdf](https://github.com/Benchify/benchify-sdk-python/commit/6681cdf5dde39dcadfd2006194277931dc785d0e))
* **internal:** codegen related update ([9c77b1b](https://github.com/Benchify/benchify-sdk-python/commit/9c77b1bc44be11429ef47d60004997ac38ec1daa))
* **internal:** fix lint error on Python 3.14 ([4f8e8e8](https://github.com/Benchify/benchify-sdk-python/commit/4f8e8e8735c4e156faa4d9dba479ca5ad42bf92a))
* **internal:** make `test_proxy_environment_variables` more resilient ([46524de](https://github.com/Benchify/benchify-sdk-python/commit/46524de6bbe962ba385dd851f14bad6724a727f0))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([3e63088](https://github.com/Benchify/benchify-sdk-python/commit/3e630889266a7141a7c55608e9a82a0a9ba356da))
* **internal:** remove mock server code ([10a1f64](https://github.com/Benchify/benchify-sdk-python/commit/10a1f64f9e861aba06f334c933e9ef716b1ea141))
* **internal:** update `actions/checkout` version ([1450fbd](https://github.com/Benchify/benchify-sdk-python/commit/1450fbd5b449481749a518d3b8c1410ba8473b05))
* **package:** drop Python 3.8 support ([f5b1d6b](https://github.com/Benchify/benchify-sdk-python/commit/f5b1d6b16383e15a84a2d3a974d8fa5380a7a676))
* speedup initial import ([3791761](https://github.com/Benchify/benchify-sdk-python/commit/37917619e0f6b6506afa8251aaa3cb0760907886))
* update lockfile ([9a95a83](https://github.com/Benchify/benchify-sdk-python/commit/9a95a832a4bf7a3b456c8919e5b28adab0666f90))
* update mock server docs ([8c7ae7b](https://github.com/Benchify/benchify-sdk-python/commit/8c7ae7b7ef535ee037dcccd0f074348dd21b7ea1))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([73251c3](https://github.com/Benchify/benchify-sdk-python/commit/73251c34c556b8010d7c18d8f200930a9e3b1a87))

## 0.7.0 (2025-11-07)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/Benchify/benchify-sdk-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** manual updates ([e814d3a](https://github.com/Benchify/benchify-sdk-python/commit/e814d3a7c88489d0ec9c997d7b9ae072bd7d6773))

## 0.6.0 (2025-11-07)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/Benchify/benchify-sdk-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** manual updates ([d8325b9](https://github.com/Benchify/benchify-sdk-python/commit/d8325b943dd9073d7f1952c961d8a85271b52b42))

## 0.5.0 (2025-11-06)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/Benchify/benchify-sdk-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([ae7d9d1](https://github.com/Benchify/benchify-sdk-python/commit/ae7d9d16420bd8f6625fd257db57acddf421270c))
* **api:** api update ([a278466](https://github.com/Benchify/benchify-sdk-python/commit/a2784662fb93313c7a24235c8a8f7ab84342cb03))
* **api:** manual updates ([d9d38bc](https://github.com/Benchify/benchify-sdk-python/commit/d9d38bc9988ae9d68f051dc4c742cb5ac56e173d))

## 0.4.0 (2025-11-04)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/Benchify/benchify-sdk-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([2fca93d](https://github.com/Benchify/benchify-sdk-python/commit/2fca93d5c2ac0902afef89f4b373f651c7dc9e09))
* **api:** api update ([99eb6bc](https://github.com/Benchify/benchify-sdk-python/commit/99eb6bc604beb9a79122c12bbd54d26246757a32))
* **api:** api update ([ebe5ab6](https://github.com/Benchify/benchify-sdk-python/commit/ebe5ab6c699597bcab9b724824d7e023997cc28f))
* **api:** api update ([d30f799](https://github.com/Benchify/benchify-sdk-python/commit/d30f79937767f227ff418efc5ccac45b1e00b25e))
* **api:** api update ([34cc723](https://github.com/Benchify/benchify-sdk-python/commit/34cc723eed838f2d2eefc670436fb16eb3c22ce8))
* **api:** api update ([3de5719](https://github.com/Benchify/benchify-sdk-python/commit/3de57191bf38bdb91e8bbb2f389c4b76bf137ba4))
* **api:** api update ([9050e1b](https://github.com/Benchify/benchify-sdk-python/commit/9050e1b58e45da38f220d431fddff5db166fbe00))
* **api:** api update ([a5560f0](https://github.com/Benchify/benchify-sdk-python/commit/a5560f0646bec6ad3c1bae215f5b1fb5c41c478a))
* **api:** api update ([bf04812](https://github.com/Benchify/benchify-sdk-python/commit/bf048125fda2fd3225340f42b89c376150dd4daa))
* **api:** api update ([e9e1b7d](https://github.com/Benchify/benchify-sdk-python/commit/e9e1b7dbdfa4b949c4e8fef70944d50db2df9949))
* **api:** api update ([f2f4626](https://github.com/Benchify/benchify-sdk-python/commit/f2f46266131296b4b9c38707e3dac0199e559a94))
* **api:** api update ([bc6e9ee](https://github.com/Benchify/benchify-sdk-python/commit/bc6e9eed6f0e89a61a3ab7433c7294c226483654))
* **api:** api update ([10e71e9](https://github.com/Benchify/benchify-sdk-python/commit/10e71e9671deda927d729ed942997b18625473d5))
* **api:** api update ([e2305a2](https://github.com/Benchify/benchify-sdk-python/commit/e2305a2797d334d61cb9d734a957935f46a28eb2))
* **api:** api update ([f6c8447](https://github.com/Benchify/benchify-sdk-python/commit/f6c8447c4910f268980a463f0746ee766a17dd58))
* **api:** api update ([b148e30](https://github.com/Benchify/benchify-sdk-python/commit/b148e305669d89eeaa9857149c13bf11101bd53e))
* **api:** manual updates ([6535638](https://github.com/Benchify/benchify-sdk-python/commit/65356381c301dd23cca90a0efbdd6841f7cf2ff0))
* **api:** manual updates ([df63e8f](https://github.com/Benchify/benchify-sdk-python/commit/df63e8febc4a33ac5c94fc56429fd30405faeb50))
* **api:** manual updates ([cafecda](https://github.com/Benchify/benchify-sdk-python/commit/cafecdab25d1f9575a9180a36ac1b55786a23493))
* **api:** manual updates ([3d7a1a9](https://github.com/Benchify/benchify-sdk-python/commit/3d7a1a9c7c19aaeb9f4b0e96586865faa5c04caa))
* **api:** manual updates ([df0af9d](https://github.com/Benchify/benchify-sdk-python/commit/df0af9d41cfaa4950697a2ce12b9d900013dad10))
* **api:** manual updates ([91e5474](https://github.com/Benchify/benchify-sdk-python/commit/91e5474eef8dfb630e52ec72bb5f3bec7fda532a))
* **api:** manual updates ([b756361](https://github.com/Benchify/benchify-sdk-python/commit/b7563617ba095bd4e5569fd0f7002bd32a809cb7))
* **api:** manual updates ([6962c6c](https://github.com/Benchify/benchify-sdk-python/commit/6962c6c6984d0951aa9fe1b0160fed270b107093))
* **api:** manual updates ([c4b7522](https://github.com/Benchify/benchify-sdk-python/commit/c4b752230262cb47b30cd667a632fa5779c895e2))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([e9758b0](https://github.com/Benchify/benchify-sdk-python/commit/e9758b00c094d14302ee3d44d5397f4d9e3c0bb4))
* do not install brew dependencies in ./scripts/bootstrap by default ([5272e8d](https://github.com/Benchify/benchify-sdk-python/commit/5272e8d204fab36f2f0b1c4223b98f84393dc2e9))
* **internal:** codegen related update ([932d424](https://github.com/Benchify/benchify-sdk-python/commit/932d424b395e04ed07ec68ae30ad20678f41b700))
* **internal:** detect missing future annotations with ruff ([4951593](https://github.com/Benchify/benchify-sdk-python/commit/49515932520506b070e2fc7108f104cc231f9ee6))
* **internal:** grammar fix (it's -&gt; its) ([ad99bb8](https://github.com/Benchify/benchify-sdk-python/commit/ad99bb837d88662133915b2669f35f2920b8bc84))
* **types:** change optional parameter type from NotGiven to Omit ([2a03d51](https://github.com/Benchify/benchify-sdk-python/commit/2a03d516e810d5811750e7e89120957e4e372096))

## 0.3.0 (2025-08-18)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/Benchify/benchify-sdk-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([61c8d1b](https://github.com/Benchify/benchify-sdk-python/commit/61c8d1b4f0d79570c17ff2d70362d6f1d4dba623))

## 0.2.0 (2025-08-18)

Full Changelog: [v0.1.3...v0.2.0](https://github.com/Benchify/benchify-sdk-python/compare/v0.1.3...v0.2.0)

### Features

* **api:** api update ([d02ae03](https://github.com/Benchify/benchify-sdk-python/commit/d02ae03649ef0970a556c301f03279fcce34768a))
* **api:** api update ([429df1a](https://github.com/Benchify/benchify-sdk-python/commit/429df1a7e793d18ca7160acb424ef0f95d0fea54))
* **api:** api update ([d1e52a2](https://github.com/Benchify/benchify-sdk-python/commit/d1e52a2d248db65cfaea5e1f330043d71def9ab2))


### Chores

* **internal:** codegen related update ([3d981f1](https://github.com/Benchify/benchify-sdk-python/commit/3d981f1e780b2cf74fbe5c9244b3488c923d5518))

## 0.1.3 (2025-08-11)

Full Changelog: [v0.0.1...v0.1.3](https://github.com/Benchify/benchify-sdk-python/compare/v0.0.1...v0.1.3)

### Chores

* configure new SDK language ([b2947a6](https://github.com/Benchify/benchify-sdk-python/commit/b2947a6d28b64d77a43add29773e1f5044a4b793))
* update SDK settings ([6744a08](https://github.com/Benchify/benchify-sdk-python/commit/6744a084c082925416efd1f4eaf2a3fa6319a8fe))
* update SDK settings ([94d44df](https://github.com/Benchify/benchify-sdk-python/commit/94d44dfa86ec52e67c81c1bce48f7551cdd2e551))
