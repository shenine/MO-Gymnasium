from gymnasium.envs.registration import register


register(
    id="resource-gathering-v0",
    entry_point="mo_gymnasium.envs.resource_gathering.resource_gathering:ResourceGathering",
    max_episode_steps=100,
)

register(
    id="resource-gathering-v1",
    entry_point="mo_gymnasium.envs.resource_gathering.resource_gathering_1:ResourceGathering",
    max_episode_steps=100,
)

register(
    id="resource-gathering-v2",
    entry_point="mo_gymnasium.envs.resource_gathering.resource_gathering_2:ResourceGathering",
    max_episode_steps=500,
)

register(
    id="resource-gathering-singleO",
    entry_point="mo_gymnasium.envs.resource_gathering.resource_gathering_singleO:ResourceGathering",
    max_episode_steps=500,
)