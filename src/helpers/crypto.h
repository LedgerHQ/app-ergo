
#pragma once

#include <stdint.h>  // uint*_t

#include <os.h>
#include <cx.h>
#include "constants.h"

/**
 * Derive private key given BIP32 path.
 *
 * @param[out] private_key
 *   Pointer to private key.
 * @param[out] chain_code
 *   Pointer to 32 bytes array for chain code.
 * @param[in]  bip32_path
 *   Pointer to buffer with BIP32 path.
 * @param[in]  bip32_path_len
 *   Number of path in BIP32 path.
 *
 * @throw INVALID_PARAMETER
 *
 */
void crypto_derive_private_key(cx_ecfp_private_key_t *private_key,
                               uint8_t chain_code[static CHAIN_CODE_LEN],
                               const uint32_t *bip32_path,
                               uint8_t bip32_path_len);

/**
 * Initialize public key given private key.
 *
 * @param[in]  private_key
 *   Pointer to private key.
 * @param[out] public_key
 *   Pointer to public key.
 * @param[out] raw_public_key
 *   Pointer to raw public key.
 *
 * @throw INVALID_PARAMETER
 *
 */
void crypto_init_public_key(cx_ecfp_private_key_t *private_key,
                            cx_ecfp_public_key_t *public_key,
                            uint8_t raw_public_key[static PUBLIC_KEY_LEN]);

void crypto_generate_public_key(const uint32_t *bip32_path,
                                uint8_t bip32_path_len,
                                uint8_t raw_public_key[static PUBLIC_KEY_LEN],
                                uint8_t chain_code[CHAIN_CODE_LEN]);
