from typing import NamedTuple

from promise import Promise
from promise.dataloader import DataLoader


class PersonProfilePictureLoader(DataLoader):
    # A dataloader does nothing more than batch load things.
    # All that's required is to implement this method here.
    # it takes in a list of keys and is expected to return
    # (a promised-wrapped) parallel array of values/objects.
    # If a key does not produce a valid value, then it should
    # be some sort of a sentinel to indicate as such (None works).
    # Once this method is implemented, then the `.load(key)` and
    # `.load_many(keys)` methods are available on the loader.
    # Note that you can set a `max_batch_size` class-level variable
    # (or pass it in to the constructor of the loader) to set how large
    # you want the batch size to be. E.g., since the below method is
    # pretending to make a REST call using query params, if too many
    # query params are passed, it will probably exceed some max URL
    # length, so it may need to be batched in smaller batches. Setting
    # a `max_batch_size` will automatically chunk and this method N-chunk
    # times.
    def batch_load_fn(self, person_ids):
        # resp = request.get(URL, params={'person_id': person_ids})
        # if not resp.ok:
        #     raise SomethingBadHappened()
        # data = resp.json()
        data = {
            1: 'https://profilepics.company.com/users/1',
            2: 'https://profilepics.company.com/users/2',
        }

        return Promise.resolve([data[pid] for pid in person_ids])


class Loaders(NamedTuple):
    person_profile_pictures: PersonProfilePictureLoader


def get_dataloaders():
    # if you get a lot of loaders, you can do something like this:
    #     return Loaders(
    #         # for each (attribute, type) pair declared in the Loaders
    #         # class above, instantiate the loader and pass to the Loaders
    #         # named tuple class here.
    #         **{
    #             name: loader()
    #             for name, loader in typing.get_type_hints(Loaders).items()
    #         }
    #     )
    # which will automatically instantiate all of the loaders that are registered as
    # types on the `Loaders` named tuple. But, for now and for better understanding of
    # what this function is doing, here is the simple, readable version:
    return Loaders(
        person_profile_pictures=PersonProfilePictureLoader(),
    )
