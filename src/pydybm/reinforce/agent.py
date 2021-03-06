#!/usr/bin/env python
"""
Base class for a reinforcement learning agent

__Author__: Sakyasingha Dasgupta
__copyright__ = "(C) Copyright IBM Corp. 2016"
"""


# Agent abstractions
class Agent(object):
    """The Reinforcement learning agent BaseClass.

    The main methods that users of this class need to know are:
        fit
        fit_episode
        predict

    When implementing an environment, override the following methods
    in your subclass:
        _fit
        _fit_episode
        _predict

    """

    def __new__(cls, *args, **kwargs):
        # We use __new__ since we want the env author to be able to
        # override __init__ without remembering to call super.
        env = super(Agent, cls).__new__(cls)

        # Will be automatically set when creating an environment via 'make'
        return env

    # Override in ALL subclasses
    def _fit(self, test_every, test_num_eps, break_reward, render):
        raise NotImplementedError

    def _fit_episode(self, episode, test_every, test_num_eps, break_reward):
        raise NotImplementedError

    def _predict(self, render):
        raise NotImplementedError

    def fit(self, test_every, test_num_eps, break_reward, render):
        """
        Run the training algorithm
        """
        return self._fit(test_every, test_num_eps, break_reward, render)

    def fit_episode(self):
        """
        Run the training algorithm for 1 step
        """
        return self._fit_episode()

    def predict(self, render=True):
        """
        Test the training algo
        """
        return self._predict(render)
