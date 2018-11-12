# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .MoneroRingCtSig import MoneroRingCtSig


class MoneroTransactionAllOutSetAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 514

    def __init__(
        self,
        extra: bytes = None,
        tx_prefix_hash: bytes = None,
        rv: MoneroRingCtSig = None,
        full_message_hash: bytes = None,
    ) -> None:
        self.extra = extra
        self.tx_prefix_hash = tx_prefix_hash
        self.rv = rv
        self.full_message_hash = full_message_hash

    @classmethod
    def get_fields(cls):
        return {
            1: ('extra', p.BytesType, 0),
            2: ('tx_prefix_hash', p.BytesType, 0),
            4: ('rv', MoneroRingCtSig, 0),
            5: ('full_message_hash', p.BytesType, 0),
        }