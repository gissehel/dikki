#!/usr/bin/env python3
# coding: utf-8

class RawDockerMock(object):
    def __init__(self):

        self._images = [
            {'Created': 1417763971, 'VirtualSize': 573022374, 'ParentId': '39ff3354c95404daf45b2a49d4d3993b625db3fa467683ac74ed7393663ae7cb', 'RepoTags': ['dockerfile/ghost:latest'], 'Id': 'c0243223464e8c328fc3aeef6a158cebc92b6c48ef0a1dc7c023b330c4fa906f', 'Size': 0},
            {'Created': 1417763962, 'VirtualSize': 573022374, 'ParentId': '75753ccb28c2504843f30acaae64f5635ee0d937f9f0b6a39549cc44acc9f4d1', 'RepoTags': ['<none>:<none>'], 'Id': '39ff3354c95404daf45b2a49d4d3993b625db3fa467683ac74ed7393663ae7cb', 'Size': 0},
            {'Created': 1417763954, 'VirtualSize': 573022374, 'ParentId': '2a10727e325963225e005b4f2f20a7ff136ef676d08e1498b2b79891d408ab79', 'RepoTags': ['<none>:<none>'], 'Id': '75753ccb28c2504843f30acaae64f5635ee0d937f9f0b6a39549cc44acc9f4d1', 'Size': 0},
            {'Created': 1417763947, 'VirtualSize': 573022374, 'ParentId': '0d920cb5e41f14eba1c7a2bc61ba0a111b05b1ef5001b0b1df4860ef36bbee4a', 'RepoTags': ['<none>:<none>'], 'Id': '2a10727e325963225e005b4f2f20a7ff136ef676d08e1498b2b79891d408ab79', 'Size': 0},
            {'Created': 1417763939, 'VirtualSize': 573022374, 'ParentId': '3a375b17c9c9cc229081d54511dd9c0d1a2411dd8d7fa542508db81d6b7b7414', 'RepoTags': ['<none>:<none>'], 'Id': '0d920cb5e41f14eba1c7a2bc61ba0a111b05b1ef5001b0b1df4860ef36bbee4a', 'Size': 0},
            {'Created': 1417763931, 'VirtualSize': 573022374, 'ParentId': '282a56297ac824dd33b877af8410a9da5d2d244842b38bd32e8086899c194ae5', 'RepoTags': ['<none>:<none>'], 'Id': '3a375b17c9c9cc229081d54511dd9c0d1a2411dd8d7fa542508db81d6b7b7414', 'Size': 880},
            {'Created': 1417763921, 'VirtualSize': 573021494, 'ParentId': 'c082805956506491674ecbd4ddfae7672fb5e36a96e5edd912ef1680a1de408a', 'RepoTags': ['<none>:<none>'], 'Id': '282a56297ac824dd33b877af8410a9da5d2d244842b38bd32e8086899c194ae5', 'Size': 76718234},
            {'Created': 1417763239, 'VirtualSize': 496303260, 'ParentId': 'ccceaca2d14cbd074bf727706f7b6fe755db44b56cce535647da7dd5f3897be0', 'RepoTags': ['dockerfile/nodejs:latest'], 'Id': 'c082805956506491674ecbd4ddfae7672fb5e36a96e5edd912ef1680a1de408a', 'Size': 0},
            {'Created': 1417763233, 'VirtualSize': 496303260, 'ParentId': '0a9f07d648adaccdc32e601b5eeedaaf37ff585e8da0bb877727a04457cb2f32', 'RepoTags': ['<none>:<none>'], 'Id': 'ccceaca2d14cbd074bf727706f7b6fe755db44b56cce535647da7dd5f3897be0', 'Size': 0},
            {'Created': 1417763226, 'VirtualSize': 496303260, 'ParentId': 'f08c82e36872e4aebdff28bf82c721ce18c8ea57fdce3a11aa09877dcca5056b', 'RepoTags': ['<none>:<none>'], 'Id': '0a9f07d648adaccdc32e601b5eeedaaf37ff585e8da0bb877727a04457cb2f32', 'Size': 25261064},
            {'Created': 1417762723, 'VirtualSize': 482981471, 'ParentId': 'bc1366ff5694527807b7f6f5612e1412d82b8cabde18ce6353cb08485f8a1e45', 'RepoTags': ['dockerfile/ansible:latest'], 'Id': '32a7d82ef0adf46bacbe2e62aa73d4ce97dee4d2b205d88553f7112cc8718378', 'Size': 0},
            {'Created': 1417762717, 'VirtualSize': 482981471, 'ParentId': '31abc03e444cce593689c31c6966e0a692b3cf9d5e88aaa2689ad20e26abdcc1', 'RepoTags': ['<none>:<none>'], 'Id': 'bc1366ff5694527807b7f6f5612e1412d82b8cabde18ce6353cb08485f8a1e45', 'Size': 0},
            {'Created': 1417762711, 'VirtualSize': 482981471, 'ParentId': 'f08c82e36872e4aebdff28bf82c721ce18c8ea57fdce3a11aa09877dcca5056b', 'RepoTags': ['<none>:<none>'], 'Id': '31abc03e444cce593689c31c6966e0a692b3cf9d5e88aaa2689ad20e26abdcc1', 'Size': 11939275},
            {'Created': 1417761395, 'VirtualSize': 666347086, 'ParentId': '496403f78713d0bd63e356ac5e6498209bde5b5e6454f5add0ee37ee5021ad14', 'RepoTags': ['dockerfile/mariadb:latest'], 'Id': 'e6e9537db9f50a8c1f6f3796c8b623e8584c270eeaf43338f8b3e4be4692f01d', 'Size': 0},
            {'Created': 1417761390, 'VirtualSize': 666347086, 'ParentId': 'a8b924cf59c6369ca616f29d10166cb81fd25c615442c6f85aaac38dcd0d28fc', 'RepoTags': ['<none>:<none>'], 'Id': '496403f78713d0bd63e356ac5e6498209bde5b5e6454f5add0ee37ee5021ad14', 'Size': 0},
            {'Created': 1417761386, 'VirtualSize': 666347086, 'ParentId': 'cfe1a5658613cdd832af3a8a0e107f36fa63eaf800bdf2aad303ecde485439d4', 'RepoTags': ['<none>:<none>'], 'Id': 'a8b924cf59c6369ca616f29d10166cb81fd25c615442c6f85aaac38dcd0d28fc', 'Size': 0},
            {'Created': 1417761381, 'VirtualSize': 666347086, 'ParentId': '97d5ee92247b5c568046c85ccc97724a5bba837a2b1bd573c1b920c0fc6e3ec4', 'RepoTags': ['<none>:<none>'], 'Id': 'cfe1a5658613cdd832af3a8a0e107f36fa63eaf800bdf2aad303ecde485439d4', 'Size': 0},
            {'Created': 1417761375, 'VirtualSize': 666347086, 'ParentId': 'c8f87bf54eb22e99ec3faf7e90c151b9cb3b7d6dd0c00840d6bdb0c9e0075f1c', 'RepoTags': ['<none>:<none>'], 'Id': '97d5ee92247b5c568046c85ccc97724a5bba837a2b1bd573c1b920c0fc6e3ec4', 'Size': 251720197},
            {'Created': 1417761328, 'VirtualSize': 706384587, 'ParentId': '59ecccc98652a57636f983a6de338f155a79a062df3c6bc3c321a63feb29aba9', 'RepoTags': ['dockerfile/mongodb:latest'], 'Id': 'a8806f0dd0592860d936bbb8cc93ecc8e498f546e8900aa28f8cd2aca4f99fbd', 'Size': 0},
            {'Created': 1417761324, 'VirtualSize': 706384587, 'ParentId': '856c44ffc3f82d8a16e1db5384634f6c0dc47f63085fa79f53561416640baeca', 'RepoTags': ['<none>:<none>'], 'Id': '59ecccc98652a57636f983a6de338f155a79a062df3c6bc3c321a63feb29aba9', 'Size': 0},
            {'Created': 1417761319, 'VirtualSize': 706384587, 'ParentId': '6d62a973d81dfa023841edbd70db76bb98c5cdf6a765ae397eb3349114ba46ac', 'RepoTags': ['<none>:<none>'], 'Id': '856c44ffc3f82d8a16e1db5384634f6c0dc47f63085fa79f53561416640baeca', 'Size': 0},
            {'Created': 1417761314, 'VirtualSize': 706384587, 'ParentId': 'b7dfe54cfbe19013a8623633d545e5b9c874fe6f608bc6ef93048239622f201a', 'RepoTags': ['<none>:<none>'], 'Id': '6d62a973d81dfa023841edbd70db76bb98c5cdf6a765ae397eb3349114ba46ac', 'Size': 0},
            {'Created': 1417761309, 'VirtualSize': 706384587, 'ParentId': 'ec09909136b941f2860e46522bdbc05086515d27ab0f7fbfe4c27a1593b28a2f', 'RepoTags': ['<none>:<none>'], 'Id': 'b7dfe54cfbe19013a8623633d545e5b9c874fe6f608bc6ef93048239622f201a', 'Size': 0},
            {'Created': 1417761304, 'VirtualSize': 706384587, 'ParentId': 'c8f87bf54eb22e99ec3faf7e90c151b9cb3b7d6dd0c00840d6bdb0c9e0075f1c', 'RepoTags': ['<none>:<none>'], 'Id': 'ec09909136b941f2860e46522bdbc05086515d27ab0f7fbfe4c27a1593b28a2f', 'Size': 291757698},
            {'Created': 1417761269, 'VirtualSize': 471042196, 'ParentId': '81d305e05cc4ad136dd4daaa8a875396164f61e40c41419b7a3a0f22684d604b', 'RepoTags': ['dockerfile/python:latest'], 'Id': 'f08c82e36872e4aebdff28bf82c721ce18c8ea57fdce3a11aa09877dcca5056b', 'Size': 0},
            {'Created': 1417761264, 'VirtualSize': 471042196, 'ParentId': '553426e5855240104fa4bf039b3416fe2e99de29bffce04339e479ad6137ebf1', 'RepoTags': ['<none>:<none>'], 'Id': '81d305e05cc4ad136dd4daaa8a875396164f61e40c41419b7a3a0f22684d604b', 'Size': 0},
            {'Created': 1417761258, 'VirtualSize': 471042196, 'ParentId': 'c8f87bf54eb22e99ec3faf7e90c151b9cb3b7d6dd0c00840d6bdb0c9e0075f1c', 'RepoTags': ['<none>:<none>'], 'Id': '553426e5855240104fa4bf039b3416fe2e99de29bffce04339e479ad6137ebf1', 'Size': 56415307},
            {'Created': 1417759178, 'VirtualSize': 414626889, 'ParentId': '7bc005b1a6b8c2cebba0710c4dc0088531f62899ad371a8f545ef71764af2b4e', 'RepoTags': ['dockerfile/ubuntu:latest'], 'Id': 'c8f87bf54eb22e99ec3faf7e90c151b9cb3b7d6dd0c00840d6bdb0c9e0075f1c', 'Size': 0},
            {'Created': 1417759173, 'VirtualSize': 414626889, 'ParentId': '46becf174ec3ab46c142b8ce42147affe8b4558edc8fa4aeca5193800eea7c3f', 'RepoTags': ['<none>:<none>'], 'Id': '7bc005b1a6b8c2cebba0710c4dc0088531f62899ad371a8f545ef71764af2b4e', 'Size': 0},
            {'Created': 1417759168, 'VirtualSize': 414626889, 'ParentId': '0b88dc84850d40671bd62f33217055d8b96a056eff49684fbd3d0d51ba385243', 'RepoTags': ['<none>:<none>'], 'Id': '46becf174ec3ab46c142b8ce42147affe8b4558edc8fa4aeca5193800eea7c3f', 'Size': 0},
            {'Created': 1417759163, 'VirtualSize': 414626889, 'ParentId': 'd137c5918ab752b98b6c2ae41bf6045e84299c4973d450033e6a5f84c06b3c6b', 'RepoTags': ['<none>:<none>'], 'Id': '0b88dc84850d40671bd62f33217055d8b96a056eff49684fbd3d0d51ba385243', 'Size': 80574},
            {'Created': 1417759158, 'VirtualSize': 414546315, 'ParentId': '3f76613d5c23f428f7de9ed6073ed1d16b200c8b2cf5101196d96e307edd65aa', 'RepoTags': ['<none>:<none>'], 'Id': 'd137c5918ab752b98b6c2ae41bf6045e84299c4973d450033e6a5f84c06b3c6b', 'Size': 532},
            {'Created': 1417759152, 'VirtualSize': 414545783, 'ParentId': '55a37ec28b4561ae326ee760e592f6c36a63c14150b31610ec1ca7f4ccecb9a9', 'RepoTags': ['<none>:<none>'], 'Id': '3f76613d5c23f428f7de9ed6073ed1d16b200c8b2cf5101196d96e307edd65aa', 'Size': 1122},
            {'Created': 1417759144, 'VirtualSize': 414544661, 'ParentId': '9bd07e480c5b152fbd561f6083e3b70299f40f914dc6ff9b134740364a8a27a6', 'RepoTags': ['<none>:<none>'], 'Id': '55a37ec28b4561ae326ee760e592f6c36a63c14150b31610ec1ca7f4ccecb9a9', 'Size': 221864163},
            {'Created': 1417715911, 'VirtualSize': 192680498, 'ParentId': 'e1cdf371fbdeaa08209e7c7af2fec6764f471402b193040e97fc224715250a11', 'RepoTags': ['ubuntu:14.04', 'ubuntu:latest', 'ubuntu:14.04-20141204'], 'Id': '9bd07e480c5b152fbd561f6083e3b70299f40f914dc6ff9b134740364a8a27a6', 'Size': 0},
            {'Created': 1417715910, 'VirtualSize': 192680498, 'ParentId': '30541f8f306240e9fe78bc82f89f1c16c00f3ff4c90cf8a6f750d5a703b49950', 'RepoTags': ['<none>:<none>'], 'Id': 'e1cdf371fbdeaa08209e7c7af2fec6764f471402b193040e97fc224715250a11', 'Size': 1895},
            {'Created': 1417715908, 'VirtualSize': 192678603, 'ParentId': '01bf15a18638145eb44f0363ece1845b0f0dcf24adc03700ca519ea3d5fe6b0e', 'RepoTags': ['<none>:<none>'], 'Id': '30541f8f306240e9fe78bc82f89f1c16c00f3ff4c90cf8a6f750d5a703b49950', 'Size': 194791},
            {'Created': 1417715902, 'VirtualSize': 192483812, 'ParentId': '511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158', 'RepoTags': ['<none>:<none>'], 'Id': '01bf15a18638145eb44f0363ece1845b0f0dcf24adc03700ca519ea3d5fe6b0e', 'Size': 192483812},
            {'Created': 1417041048, 'VirtualSize': 812635892, 'ParentId': '7b46d54695b8c34e9fbf5715e59f9c956ad506fdd6f0d1f2982064b564bd906f', 'RepoTags': ['python:2.7'], 'Id': '481b175a31dbc80ce5d4445b97b132533469981611c933388e1a02b697b50d70', 'Size': 0},
            {'Created': 1417041046, 'VirtualSize': 812635892, 'ParentId': 'ef5cb5050906092d0742f95427b6a94072dbde76d63933b465ab5adb1112f011', 'RepoTags': ['<none>:<none>'], 'Id': '7b46d54695b8c34e9fbf5715e59f9c956ad506fdd6f0d1f2982064b564bd906f', 'Size': 5364041},
            {'Created': 1417041041, 'VirtualSize': 807271851, 'ParentId': '2b954b1bd956cd856671802fccf608c2aac8cf4a04b6e432f6d2cb5184f7a205', 'RepoTags': ['<none>:<none>'], 'Id': 'ef5cb5050906092d0742f95427b6a94072dbde76d63933b465ab5adb1112f011', 'Size': 57830889},
            {'Created': 1417040859, 'VirtualSize': 749440962, 'ParentId': '726152d818e90af6d6e456d3204033ad8cca2873a1960f6c22c0d1d16cf438b5', 'RepoTags': ['<none>:<none>'], 'Id': '2b954b1bd956cd856671802fccf608c2aac8cf4a04b6e432f6d2cb5184f7a205', 'Size': 0},
            {'Created': 1417040858, 'VirtualSize': 749440962, 'ParentId': 'c006144703200dd9df14fdf7febb3bc340f0a8f5538ab57a4e6715bba89227e2', 'RepoTags': ['<none>:<none>'], 'Id': '726152d818e90af6d6e456d3204033ad8cca2873a1960f6c22c0d1d16cf438b5', 'Size': 0},
            {'Created': 1417040856, 'VirtualSize': 749440962, 'ParentId': 'ea9819f761f174724f5f05712235b2bcf535bd5e05b476286fd5e46864f58768', 'RepoTags': ['<none>:<none>'], 'Id': 'c006144703200dd9df14fdf7febb3bc340f0a8f5538ab57a4e6715bba89227e2', 'Size': 1494923},
            {'Created': 1416854996, 'VirtualSize': 747946039, 'ParentId': '8f3e5f544a175edaf28ee2f44477dc40cfd15922e1edfcf024761687f705c251', 'RepoTags': ['<none>:<none>'], 'Id': 'ea9819f761f174724f5f05712235b2bcf535bd5e05b476286fd5e46864f58768', 'Size': 360372594},
            {'Created': 1416854914, 'VirtualSize': 387573445, 'ParentId': 'f99c114b8ec17cf509ec78ab7f490fe4cd984098d825cf74e7a0adea849a19dd', 'RepoTags': ['<none>:<none>'], 'Id': '8f3e5f544a175edaf28ee2f44477dc40cfd15922e1edfcf024761687f705c251', 'Size': 32003007},
            {'Created': 1416854900, 'VirtualSize': 355570438, 'ParentId': 'aaabd2b41e22543a7b230c2c892a482e80f99039209b193bdd2b67a526996b30', 'RepoTags': ['<none>:<none>'], 'Id': 'f99c114b8ec17cf509ec78ab7f490fe4cd984098d825cf74e7a0adea849a19dd', 'Size': 200884448},
            {'Created': 1415518537, 'VirtualSize': 661824365, 'ParentId': 'baaa3c2b2ce6a807c1e8a5cdf5ccf68ee03e5d7cf164046a8e30df61dba1afd1', 'RepoTags': ['jenkins:1.585', 'jenkins:weekly'], 'Id': '86aa47422e9702f0aee4386ec1c1f5b80d202d3afe54e9b671332bff57f6144a', 'Size': 0},
            {'Created': 1415518536, 'VirtualSize': 661823995, 'ParentId': '5a221a25bebadea307976564129f41cf81a1f143f4b819fff6b148e9c667c36f', 'RepoTags': ['<none>:<none>'], 'Id': 'd2c0ea9c8914403d81877beca1c8f09983852797ad91a3bde464a612d9a58802', 'Size': 0},
            {'Created': 1415518536, 'VirtualSize': 661824365, 'ParentId': 'd2c0ea9c8914403d81877beca1c8f09983852797ad91a3bde464a612d9a58802', 'RepoTags': ['<none>:<none>'], 'Id': 'baaa3c2b2ce6a807c1e8a5cdf5ccf68ee03e5d7cf164046a8e30df61dba1afd1', 'Size': 370},
            {'Created': 1415518535, 'VirtualSize': 661823995, 'ParentId': '3ef6335e3f51da418f8b58dc3a1a4bb192194a36d07de9c157f305f43e492e1c', 'RepoTags': ['<none>:<none>'], 'Id': '6d7d2d1e09fc584c2843a02d0832287b4dc4d0f1c175296b3e6941f3f73f7716', 'Size': 0},
            {'Created': 1415518535, 'VirtualSize': 661823995, 'ParentId': '6d7d2d1e09fc584c2843a02d0832287b4dc4d0f1c175296b3e6941f3f73f7716', 'RepoTags': ['<none>:<none>'], 'Id': '5a221a25bebadea307976564129f41cf81a1f143f4b819fff6b148e9c667c36f', 'Size': 0},
            {'Created': 1415518534, 'VirtualSize': 661823995, 'ParentId': '5eb699ca69529fced3c6b429df1a5e222cf858645e274ac7bb33a56ef4602cfe', 'RepoTags': ['<none>:<none>'], 'Id': '3ef6335e3f51da418f8b58dc3a1a4bb192194a36d07de9c157f305f43e492e1c', 'Size': 0},
            {'Created': 1415518534, 'VirtualSize': 661823995, 'ParentId': 'c996b9075693c85fdaf52214657e5111ffa837648c3b1fe70423cc2b95db9a8a', 'RepoTags': ['<none>:<none>'], 'Id': '5eb699ca69529fced3c6b429df1a5e222cf858645e274ac7bb33a56ef4602cfe', 'Size': 6992},
            {'Created': 1415518533, 'VirtualSize': 661817003, 'ParentId': '587f51973afb9842ddb58a918510dad56a83947c6cdcb919a2be4c98ce86a1fb', 'RepoTags': ['<none>:<none>'], 'Id': 'c996b9075693c85fdaf52214657e5111ffa837648c3b1fe70423cc2b95db9a8a', 'Size': 0},
            {'Created': 1415518532, 'VirtualSize': 661817003, 'ParentId': 'c36ee84f01da6a5418bd4e56ada98358285ff53ee87fbdb255b354fabd94f1c1', 'RepoTags': ['<none>:<none>'], 'Id': '587f51973afb9842ddb58a918510dad56a83947c6cdcb919a2be4c98ce86a1fb', 'Size': 67939891},
            {'Created': 1415518519, 'VirtualSize': 661752227, 'ParentId': '7f19d2345e67726ee9ba93325bf5416a85afd07eff528162d620bb4fb1db507d', 'RepoTags': ['<none>:<none>'], 'Id': 'da3243c8d9c47679bfe8b1a1aeb2d752da9024997bb40d29212928ffa10f5be8', 'Size': 370},
            {'Created': 1415518519, 'VirtualSize': 661752227, 'ParentId': 'da3243c8d9c47679bfe8b1a1aeb2d752da9024997bb40d29212928ffa10f5be8', 'RepoTags': ['jenkins:1.565.3', 'jenkins:latest'], 'Id': '459cea0cc31fed9fb97ec1ae6cd8a69b9f722c5c4403eee1a4835b85f6a8afbc', 'Size': 0},
            {'Created': 1415518518, 'VirtualSize': 661751857, 'ParentId': '76445f4c020e20886e4e3b8a128e2960b2d55e034a43e887b071e3ba27dd23e6', 'RepoTags': ['<none>:<none>'], 'Id': '7f19d2345e67726ee9ba93325bf5416a85afd07eff528162d620bb4fb1db507d', 'Size': 0},
            {'Created': 1415518518, 'VirtualSize': 661751857, 'ParentId': '3e1d6e61b8800ddace8247943ce6a414800964038fe3da16a78d3ee8238416c4', 'RepoTags': ['<none>:<none>'], 'Id': '76445f4c020e20886e4e3b8a128e2960b2d55e034a43e887b071e3ba27dd23e6', 'Size': 0},
            {'Created': 1415518518, 'VirtualSize': 661751857, 'ParentId': '40780950c5d8da84eb758221c657b1071fbff54d28344b11505cfe73d3957ae5', 'RepoTags': ['<none>:<none>'], 'Id': '3e1d6e61b8800ddace8247943ce6a414800964038fe3da16a78d3ee8238416c4', 'Size': 0},
            {'Created': 1415518517, 'VirtualSize': 661751857, 'ParentId': '7a8eb4347a3e15b9153769dc123de868eb49c8cfd7d6ac7f4bc132e28ca1cfcc', 'RepoTags': ['<none>:<none>'], 'Id': '6e956a37fac0db1c5abd4321cda6469d52fc27a1334bf10f7e485f72c65639f7', 'Size': 6992},
            {'Created': 1415518517, 'VirtualSize': 661751857, 'ParentId': '6e956a37fac0db1c5abd4321cda6469d52fc27a1334bf10f7e485f72c65639f7', 'RepoTags': ['<none>:<none>'], 'Id': '40780950c5d8da84eb758221c657b1071fbff54d28344b11505cfe73d3957ae5', 'Size': 0},
            {'Created': 1415518516, 'VirtualSize': 661744865, 'ParentId': '75f72757b58fac1de1b8dca920fafd035f9017357c30ae973d500b962432dce0', 'RepoTags': ['<none>:<none>'], 'Id': '7a8eb4347a3e15b9153769dc123de868eb49c8cfd7d6ac7f4bc132e28ca1cfcc', 'Size': 0},
            {'Created': 1415518515, 'VirtualSize': 661744865, 'ParentId': 'f24b6e5912544b1082c6bb99ff9495e6971ad3e65c7f8cfc1d2ec797d3ec8ea7', 'RepoTags': ['<none>:<none>'], 'Id': '75f72757b58fac1de1b8dca920fafd035f9017357c30ae973d500b962432dce0', 'Size': 67867753},
            {'Created': 1415306584, 'VirtualSize': 154685990, 'ParentId': '36fd425d7d8a26bb092cf3ca8c52eb8e47170363f40a3f4e37c9cad401f0e9fe', 'RepoTags': ['debian:jessie'], 'Id': 'aaabd2b41e22543a7b230c2c892a482e80f99039209b193bdd2b67a526996b30', 'Size': 0},
            {'Created': 1415306582, 'VirtualSize': 154685990, 'ParentId': '511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158', 'RepoTags': ['<none>:<none>'], 'Id': '36fd425d7d8a26bb092cf3ca8c52eb8e47170363f40a3f4e37c9cad401f0e9fe', 'Size': 154685990},
            {'Created': 1414105822, 'VirtualSize': 593876932, 'ParentId': '4c87df3aff819ca5b0244e75d1beb00de78335468bb8701aa2f58291fe61d50c', 'RepoTags': ['<none>:<none>'], 'Id': '29da8066531d08fab96e866d6bb272ed7f97ab0756a6fddbbb9e54bcdf5b00b6', 'Size': 335486},
            {'Created': 1414105822, 'VirtualSize': 593877112, 'ParentId': '29da8066531d08fab96e866d6bb272ed7f97ab0756a6fddbbb9e54bcdf5b00b6', 'RepoTags': ['<none>:<none>'], 'Id': 'c36ee84f01da6a5418bd4e56ada98358285ff53ee87fbdb255b354fabd94f1c1', 'Size': 180},
            {'Created': 1414105822, 'VirtualSize': 593541446, 'ParentId': '89bca11769486cc770a2d44303ad9b7ff6333a68b7b310938a59cd1aad8356da', 'RepoTags': ['<none>:<none>'], 'Id': '4c87df3aff819ca5b0244e75d1beb00de78335468bb8701aa2f58291fe61d50c', 'Size': 0},
            {'Created': 1414105821, 'VirtualSize': 593541446, 'ParentId': 'c15d04694341524c8c0f3af44695d512e4004b1b2d78737463cf35e84c071f69', 'RepoTags': ['<none>:<none>'], 'Id': '89bca11769486cc770a2d44303ad9b7ff6333a68b7b310938a59cd1aad8356da', 'Size': 0},
            {'Created': 1414105781, 'VirtualSize': 593876932, 'ParentId': '91f41f5cecb26d375a4eeec243430e97177721e33e0d0db62944e4186dba1ea8', 'RepoTags': ['<none>:<none>'], 'Id': 'c0f735c606df3df5b896fbcbd879d3c3166653312f4a65c017f2f473b239d1ea', 'Size': 335486},
            {'Created': 1414105781, 'VirtualSize': 593877112, 'ParentId': 'c0f735c606df3df5b896fbcbd879d3c3166653312f4a65c017f2f473b239d1ea', 'RepoTags': ['<none>:<none>'], 'Id': 'f24b6e5912544b1082c6bb99ff9495e6971ad3e65c7f8cfc1d2ec797d3ec8ea7', 'Size': 180},
            {'Created': 1414105780, 'VirtualSize': 593541446, 'ParentId': '1d17c9a253acc2887ba4878005295624858c3e9e4c657ede7e270618f00b7fd8', 'RepoTags': ['<none>:<none>'], 'Id': '91f41f5cecb26d375a4eeec243430e97177721e33e0d0db62944e4186dba1ea8', 'Size': 0},
            {'Created': 1414105780, 'VirtualSize': 593541446, 'ParentId': 'c15d04694341524c8c0f3af44695d512e4004b1b2d78737463cf35e84c071f69', 'RepoTags': ['<none>:<none>'], 'Id': '1d17c9a253acc2887ba4878005295624858c3e9e4c657ede7e270618f00b7fd8', 'Size': 0},
            {'Created': 1414105779, 'VirtualSize': 593541446, 'ParentId': 'bd8bd16075a0187a0f735d5424dd3b3a4cfff96d7d91439fa46dbe37ab312faf', 'RepoTags': ['<none>:<none>'], 'Id': 'c15d04694341524c8c0f3af44695d512e4004b1b2d78737463cf35e84c071f69', 'Size': 30757727},
            {'Created': 1414105451, 'VirtualSize': 562783719, 'ParentId': '34664741b33ff63606fdd7ae94508aad79ade9d4daf9e6342f707c5485a646c0', 'RepoTags': ['java:openjdk-7u65-jdk'], 'Id': 'bd8bd16075a0187a0f735d5424dd3b3a4cfff96d7d91439fa46dbe37ab312faf', 'Size': 440919483},
            {'Created': 1413847423, 'VirtualSize': 121864236, 'ParentId': '71d9d77ae89e48a71f70e506df140d7aba8649c8f60ba02cb9fea003b73f0de0', 'RepoTags': ['<none>:<none>'], 'Id': '34664741b33ff63606fdd7ae94508aad79ade9d4daf9e6342f707c5485a646c0', 'Size': 0},
            {'Created': 1413845809, 'VirtualSize': 121864236, 'ParentId': '848d84b4b2abe0d69bd0b499bde527659c055db05ad02ab1fc4a646572a2fb7c', 'RepoTags': ['<none>:<none>'], 'Id': '71d9d77ae89e48a71f70e506df140d7aba8649c8f60ba02cb9fea003b73f0de0', 'Size': 0},
            {'Created': 1413845806, 'VirtualSize': 121864236, 'ParentId': '511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158', 'RepoTags': ['<none>:<none>'], 'Id': '848d84b4b2abe0d69bd0b499bde527659c055db05ad02ab1fc4a646572a2fb7c', 'Size': 121864236},
            {'Created': 1371157430, 'VirtualSize': 0, 'ParentId': '', 'RepoTags': ['scratch:latest', 'scratch:all'], 'Id': '511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158', 'Size': 0},
            ]
    
        self._containers = [        
            {'Status': 'Up 2 hours', 'Created': 1418544599+0*1419537499, 'Image': 'jenkins:1.565.3', 'Ports': [{'IP': '0.0.0.0', 'Type': 'tcp', 'PublicPort': 9090, 'PrivatePort': 8080}, {'Type': 'tcp', 'PrivatePort': 50000}], 'Command': '/usr/local/bin/jenkins.sh', 'Names': ['/jovial_bardeen'], 'Id': '40ba966812dba3837cb1fcddc88d2811d1606207f6acc8aede9d5902c96fa0ca'},
            {'Status': 'Up 7 hours', 'Created': 1418528765+0*1419521665, 'Image': 'jenkins:1.565.3', 'Ports': [{'Type': 'tcp', 'PrivatePort': 50000}, {'Type': 'tcp', 'PrivatePort': 8080}], 'Command': '/usr/local/bin/jenkins.sh', 'Names': ['/nostalgic_turing'], 'Id': '1c63c1c8b94bb7733531786c62dd720afde69433efef3eb3def7e75c45860ed2'},
            {'Status': 'Up 7 hours', 'Created': 1418528731+0*1419521631, 'Image': 'ubuntu:14.04', 'Ports': [], 'Command': '/bin/bash', 'Names': ['/ubu2'], 'Id': 'e2e9ea0741ab9f91d341cb60d41dbab308ad42001f4866d7d40f831b0828ee50'},
            {'Status': 'Exited (0) 7 hours ago', 'Created': 1418528723+0*1419521623, 'Image': 'ubuntu:14.04', 'Ports': [], 'Command': '/bin/bash', 'Names': ['/ub'], 'Id': 'cfec26c45be3021d657a470da83c9531a411810f24370d77c433aa0fb35aa05c'},
            ]

        self._inspect_containers = [
            {'HostsPath': '/var/lib/docker/containers/40ba966812dba3837cb1fcddc88d2811d1606207f6acc8aede9d5902c96fa0ca/hosts', 'Created': '2014-12-25T19:58:19.988725866Z', 'Image': '459cea0cc31fed9fb97ec1ae6cd8a69b9f722c5c4403eee1a4835b85f6a8afbc', 'Args': [], 'Driver': 'aufs', 'HostConfig': {'CapDrop': None, 'PortBindings': {'8080/tcp': [{'HostPort': '9090', 'HostIp': ''}]}, 'NetworkMode': 'bridge', 'Links': None, 'LxcConf': [], 'ContainerIDFile': '', 'Devices': [], 'CapAdd': None, 'Binds': ['/opt/dockerstore/jenkins:/var/jenkins_home'], 'RestartPolicy': {'MaximumRetryCount': 0, 'Name': ''}, 'PublishAllPorts': False, 'Dns': None, 'ExtraHosts': None, 'DnsSearch': None, 'Privileged': False, 'VolumesFrom': None}, 'MountLabel': '', 'VolumesRW': {'/var/jenkins_home': True}, 'State': {'Pid': 14556, 'Paused': False, 'Running': True, 'FinishedAt': '0001-01-01T00:00:00Z', 'Restarting': False, 'StartedAt': '2014-12-25T19:58:20.139773262Z', 'ExitCode': 0}, 'ExecDriver': 'native-0.2', 'ResolvConfPath': '/var/lib/docker/containers/40ba966812dba3837cb1fcddc88d2811d1606207f6acc8aede9d5902c96fa0ca/resolv.conf', 'Volumes': {'/var/jenkins_home': '/opt/dockerstore/jenkins'}, 'Path': '/usr/local/bin/jenkins.sh', 'HostnamePath': '/var/lib/docker/containers/40ba966812dba3837cb1fcddc88d2811d1606207f6acc8aede9d5902c96fa0ca/hostname', 'ProcessLabel': '', 'Config': {'Env': ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'JAVA_VERSION=7u65', 'JENKINS_VERSION=1.565.3', 'JENKINS_HOME=/var/jenkins_home'], 'Hostname': '40ba966812db', 'Entrypoint': ['/usr/local/bin/jenkins.sh'], 'PortSpecs': None, 'Memory': 0, 'OnBuild': None, 'OpenStdin': False, 'Cpuset': '', 'User': 'jenkins', 'CpuShares': 0, 'AttachStdout': False, 'NetworkDisabled': False, 'WorkingDir': '', 'Cmd': None, 'StdinOnce': False, 'AttachStdin': False, 'MemorySwap': 0, 'Volumes': {'/var/jenkins_home': {}}, 'Tty': False, 'AttachStderr': False, 'Domainname': '', 'Image': 'jenkins:latest', 'SecurityOpt': None, 'ExposedPorts': {'8080/tcp': {}, '50000/tcp': {}}}, 'Id': '40ba966812dba3837cb1fcddc88d2811d1606207f6acc8aede9d5902c96fa0ca', 'NetworkSettings': {'MacAddress': '02:42:ac:11:02:af', 'Bridge': 'docker0', 'PortMapping': None, 'IPPrefixLen': 16, 'IPAddress': '172.17.2.175', 'Gateway': '172.17.42.1', 'Ports': {'8080/tcp': [{'HostPort': '9090', 'HostIp': '0.0.0.0'}], '50000/tcp': None}}, 'Name': '/jovial_bardeen'},
            {'HostsPath': '/var/lib/docker/containers/1c63c1c8b94bb7733531786c62dd720afde69433efef3eb3def7e75c45860ed2/hosts', 'Created': '2014-12-25T15:34:25.594231619Z', 'Image': '459cea0cc31fed9fb97ec1ae6cd8a69b9f722c5c4403eee1a4835b85f6a8afbc', 'Args': [], 'Driver': 'aufs', 'HostConfig': {'CapDrop': None, 'PortBindings': {}, 'NetworkMode': 'bridge', 'Links': None, 'LxcConf': [], 'ContainerIDFile': '', 'Devices': [], 'CapAdd': None, 'Binds': None, 'RestartPolicy': {'MaximumRetryCount': 0, 'Name': ''}, 'PublishAllPorts': False, 'Dns': None, 'ExtraHosts': None, 'DnsSearch': None, 'Privileged': False, 'VolumesFrom': None}, 'MountLabel': '', 'VolumesRW': {'/var/jenkins_home': True}, 'State': {'Pid': 32055, 'Paused': False, 'Running': True, 'FinishedAt': '0001-01-01T00:00:00Z', 'Restarting': False, 'StartedAt': '2014-12-25T15:34:25.944836213Z', 'ExitCode': 0}, 'ExecDriver': 'native-0.2', 'ResolvConfPath': '/var/lib/docker/containers/1c63c1c8b94bb7733531786c62dd720afde69433efef3eb3def7e75c45860ed2/resolv.conf', 'Volumes': {'/var/jenkins_home': '/var/lib/docker/vfs/dir/03489b3c10afd26ec569d8c4799b38e680d931ce1ee85fa97601b85fbf08f5f8'}, 'Path': '/usr/local/bin/jenkins.sh', 'HostnamePath': '/var/lib/docker/containers/1c63c1c8b94bb7733531786c62dd720afde69433efef3eb3def7e75c45860ed2/hostname', 'ProcessLabel': '', 'Config': {'Env': ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'JAVA_VERSION=7u65', 'JENKINS_VERSION=1.565.3', 'JENKINS_HOME=/var/jenkins_home'], 'Hostname': '1c63c1c8b94b', 'Entrypoint': ['/usr/local/bin/jenkins.sh'], 'PortSpecs': None, 'Memory': 0, 'OnBuild': None, 'OpenStdin': False, 'Cpuset': '', 'User': 'jenkins', 'CpuShares': 0, 'AttachStdout': False, 'NetworkDisabled': False, 'WorkingDir': '', 'Cmd': None, 'StdinOnce': False, 'AttachStdin': False, 'MemorySwap': 0, 'Volumes': {'/var/jenkins_home': {}}, 'Tty': False, 'AttachStderr': False, 'Domainname': '', 'Image': 'jenkins:latest', 'SecurityOpt': None, 'ExposedPorts': {'8080/tcp': {}, '50000/tcp': {}}}, 'Id': '1c63c1c8b94bb7733531786c62dd720afde69433efef3eb3def7e75c45860ed2', 'NetworkSettings': {'MacAddress': '02:42:ac:11:02:aa', 'Bridge': 'docker0', 'PortMapping': None, 'IPPrefixLen': 16, 'IPAddress': '172.17.2.170', 'Gateway': '172.17.42.1', 'Ports': {'8080/tcp': None, '50000/tcp': None}}, 'Name': '/nostalgic_turing'},
            {'HostsPath': '/var/lib/docker/containers/e2e9ea0741ab9f91d341cb60d41dbab308ad42001f4866d7d40f831b0828ee50/hosts', 'Created': '2014-12-25T15:33:51.197110899Z', 'Image': '04c5d3b7b0656168630d3ba35d8889bd0e9caafcaeb3004d2bfbc47e7c5d35d2', 'Args': [], 'Driver': 'aufs', 'HostConfig': {'CapDrop': None, 'PortBindings': {}, 'NetworkMode': 'bridge', 'Links': None, 'LxcConf': [], 'ContainerIDFile': '', 'Devices': [], 'CapAdd': None, 'Binds': None, 'RestartPolicy': {'MaximumRetryCount': 0, 'Name': ''}, 'PublishAllPorts': False, 'Dns': None, 'ExtraHosts': None, 'DnsSearch': None, 'Privileged': False, 'VolumesFrom': None}, 'MountLabel': '', 'VolumesRW': {}, 'State': {'Pid': 31250, 'Paused': False, 'Running': True, 'FinishedAt': '0001-01-01T00:00:00Z', 'Restarting': False, 'StartedAt': '2014-12-25T15:33:51.331895461Z', 'ExitCode': 0}, 'ExecDriver': 'native-0.2', 'ResolvConfPath': '/var/lib/docker/containers/e2e9ea0741ab9f91d341cb60d41dbab308ad42001f4866d7d40f831b0828ee50/resolv.conf', 'Volumes': {}, 'Path': '/bin/bash', 'HostnamePath': '/var/lib/docker/containers/e2e9ea0741ab9f91d341cb60d41dbab308ad42001f4866d7d40f831b0828ee50/hostname', 'ProcessLabel': '', 'Config': {'Env': ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'], 'Hostname': 'foo2', 'Entrypoint': None, 'PortSpecs': None, 'Memory': 0, 'OnBuild': None, 'OpenStdin': True, 'Cpuset': '', 'User': '', 'CpuShares': 0, 'AttachStdout': True, 'NetworkDisabled': False, 'WorkingDir': '', 'Cmd': ['/bin/bash'], 'StdinOnce': True, 'AttachStdin': True, 'MemorySwap': 0, 'Volumes': None, 'Tty': True, 'AttachStderr': True, 'Domainname': '', 'Image': 'ubuntu:trusty', 'SecurityOpt': None, 'ExposedPorts': None}, 'Id': 'e2e9ea0741ab9f91d341cb60d41dbab308ad42001f4866d7d40f831b0828ee50', 'NetworkSettings': {'MacAddress': '02:42:ac:11:02:a8', 'Bridge': 'docker0', 'PortMapping': None, 'IPPrefixLen': 16, 'IPAddress': '172.17.2.168', 'Gateway': '172.17.42.1', 'Ports': {}}, 'Name': '/ubu2'},
            {'HostsPath': '/var/lib/docker/containers/cfec26c45be3021d657a470da83c9531a411810f24370d77c433aa0fb35aa05c/hosts', 'Created': '2014-12-25T15:33:43.2336976Z', 'Image': '04c5d3b7b0656168630d3ba35d8889bd0e9caafcaeb3004d2bfbc47e7c5d35d2', 'Args': [], 'Driver': 'aufs', 'HostConfig': {'CapDrop': None, 'PortBindings': {}, 'NetworkMode': 'bridge', 'Links': None, 'LxcConf': [], 'ContainerIDFile': '', 'Devices': [], 'CapAdd': None, 'Binds': None, 'RestartPolicy': {'MaximumRetryCount': 0, 'Name': ''}, 'PublishAllPorts': False, 'Dns': None, 'ExtraHosts': None, 'DnsSearch': None, 'Privileged': False, 'VolumesFrom': None}, 'MountLabel': '', 'VolumesRW': {}, 'State': {'Pid': 0, 'Paused': False, 'Running': False, 'FinishedAt': '2014-12-25T15:33:43.979165545Z', 'Restarting': False, 'StartedAt': '2014-12-25T15:33:43.35980629Z', 'ExitCode': 0}, 'ExecDriver': 'native-0.2', 'ResolvConfPath': '/var/lib/docker/containers/cfec26c45be3021d657a470da83c9531a411810f24370d77c433aa0fb35aa05c/resolv.conf', 'Volumes': {}, 'Path': '/bin/bash', 'HostnamePath': '/var/lib/docker/containers/cfec26c45be3021d657a470da83c9531a411810f24370d77c433aa0fb35aa05c/hostname', 'ProcessLabel': '', 'Config': {'Env': ['PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'], 'Hostname': 'foo', 'Entrypoint': None, 'PortSpecs': None, 'Memory': 0, 'OnBuild': None, 'OpenStdin': True, 'Cpuset': '', 'User': '', 'CpuShares': 0, 'AttachStdout': True, 'NetworkDisabled': False, 'WorkingDir': '', 'Cmd': ['/bin/bash'], 'StdinOnce': True, 'AttachStdin': True, 'MemorySwap': 0, 'Volumes': None, 'Tty': True, 'AttachStderr': True, 'Domainname': '', 'Image': 'ubuntu:trusty', 'SecurityOpt': None, 'ExposedPorts': None}, 'Id': 'cfec26c45be3021d657a470da83c9531a411810f24370d77c433aa0fb35aa05c', 'NetworkSettings': {'MacAddress': '', 'Bridge': '', 'PortMapping': None, 'IPPrefixLen': 0, 'IPAddress': '', 'Gateway': '', 'Ports': None}, 'Name': '/ub'},
            ]

    def get_images(self):
        return self._images

    def get_containers(self):
        return self._containers

    def get_container_info(self, id):
        for container_info in self._inspect_containers:
            if container_info['Id'] == id:
                return container_info
        return None
