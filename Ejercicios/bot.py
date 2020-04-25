# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:00:11 2020

@author: claud
"""

from chatterbot import ChatBot

chatbot = ChatBot(
        "Ejemplo Bot",
        trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
        )
chatbot.train(
        "chatterbot.corpus.spanish"
        )