from ergo_lib_python.transaction import UnsignedTransaction, Transaction, UnsignedInput, Input
from ergo_lib_python.chain import Address
from ergo_lib_python.verifier import verify_signature

def chunk(array: list, size: int) -> list:
    if not array:
        return []
    if len(array) <= size:
        return [array]

    chunks = []
    for i in range(0, len(array), size):
        chunks.append(array[i:i + size])

    return chunks


def uniq(array: list) -> list:
    if not array:
        return array
    return list(dict.fromkeys(array))

def verify_signatures(unsigned: UnsignedTransaction, signatures: list[bytes], from_address: Address):
    signed = Transaction.from_unsigned_tx(unsigned, signatures)

    list_inputs: list[Input] = []
    for sinp in signed.inputs:
        input_elt = UnsignedInput(sinp.box_id)
        input_elt = Input.from_unsigned_input(input_elt, bytes())
        list_inputs.append(input_elt)

    unsigned_tx_for_prove = Transaction(list_inputs, signed.data_inputs, signed.output_candidates)

    return verify_signature(from_address, bytes(unsigned_tx_for_prove), signatures[0])
