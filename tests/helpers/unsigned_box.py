from ergo_lib_python.chain import ErgoBox, ContextExtension

class UnsignedBox:
    def __init__(self, ergo_box: ErgoBox, context_extension: ContextExtension, sign_path: str):
        self.tx_id = str(ergo_box.transaction_id)
        self.index = ergo_box.index
        self.value = ergo_box.value
        self.ergo_tree:bytes = bytes(ergo_box.ergo_tree)
        self.creation_height = ergo_box.creation_height
        self.tokens = ergo_box.tokens
        self.additional_registers = bytes(ergo_box.additional_registers)
        self.extension = bytes(context_extension) # b"" if context_extension.__len__() == 0 else context_extension)
        self.sign_path = sign_path
