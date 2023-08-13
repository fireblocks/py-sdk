from fireblocks_client.paths.tap_draft.get import ApiForget
from fireblocks_client.paths.tap_draft.put import ApiForput
from fireblocks_client.paths.tap_draft.post import ApiForpost


class TapDraft(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
