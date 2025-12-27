# --- ASSETS DICTIONARY ---
# We map words to online GIFs. 
sign_dictionary = {
    "hello": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExajhxb3Z2M2F6YTd6cWV6dHhrbzVicXVoNnBqNXB0cjE2Nm81bDA1OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKNKOfKlIhbD3gY/giphy.gif", # Generic wave
    "yes": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2RqZXA1dDZ2dDV3MTZqMHc5ZDI5dW53OWE1bjVrNjQxMHY2ajFmYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SVBqUUmmE0ZVKGbYt5/giphy.gif", # Nod
    "no": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW54M3V2dGM0Y2ExMGhocjdvNGEzMGRyNW1md3Iyb3hhcmMycDdqeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4Jz4faxuS1FiSEV2/giphy.gif", # Shake head
    "help": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGYzYzFyY2JjYTJxaHRxMGZjd254N2NkdzhnbmNubDAxZnJzZTR1aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l0MYQo0iDSTlnRifK/giphy.gif",
    "thank you": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2NrM3JtbXY4cTlsajhocXllcDZ5NmE2dG9wN3IzdW90c3g4cGE0NiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Pn0MGubCj94O2kzYvc/giphy.gif",
    "deaf": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmpieHlrbHdxcDU0OTc1Z3M0N21jbGUycnlkNmd0cHphYWRkbmVieCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKW5GfTabRXKRMI/giphy.gif",
    "goodbye": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmpieHlrbHdxcDU0OTc1Z3M0N21jbGUycnlkNmd0cHphYWRkbmVieCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKzb3i29i86BPJm/giphy.gif",
    "please": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnoxa2RsdHVmMWo5bXJwcWF2dTRpY3p3cmppd2VsbzJ0OWxrZzZ0bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ge7kt5B91FpV9NN0tb/giphy.gif",
    "sorry": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTgwM3JheHIzNm12ZWFnNWM0eWsweDI2MXQxaGtzYW1lbDR5bHFxaiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKq0oNLk8ljH7vG/giphy.gif",
    "love": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGNxZ2FiYzhsOWR6NW03MmxyNnY4NjBxNHJoczRmOHl5ZTZhcHp3YiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l4Jz6dIf7UUy4YwXm/giphy.gif",
    "name": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDY4d2poaThybXZqNjA5ZjAyazUzNG85a242dDV6eXBndnkzbGJsZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/hrXagS9iyaF29hB32n/giphy.gif",
    "what": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHoxemZneWdreHlyaXRqenBmOWJwNGUyMGZ5Z2J3Z2IyaHAzY2YyOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKN1heXwjTfwz6M/giphy.gif",
    "where": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDM4Z2ViaXJocTl6aWIxdmY1enF3amdlanJoam83eDRhODdlZjJvciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/efTrI6stUUSfXHKsVv/giphy.gif",
    "when": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDBscjc5aXF3emV1bGt6YnBkaDlqZXpqZGcyeGlhM283cHc1NTBxcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/JqJGGOcUwn4143Gy8q/giphy.gif",
    "why": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2wwZjAxNTRrdW5peW8yNDNiMHdqanhlYWYyem42bTVha2JlZ2NxYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ma6dIZ6glX5tPdRHN6/giphy.gif",
    "how": "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3eTd4Z2YzN2pjY3ByMTk0aTNreG4xbDR2NnA3Nm9sb3ZscnV4b2dlYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/RMlPljGDqzfSWxgrXE/giphy.gif",
    "good luck": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDg2amFyMTNtMWthMzUwajFnNzN0N2c5bjFlNm16dGY1NWs2djJkMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26DOD8Swx0bBWGXrq/giphy.gif",
    "bad": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExejZ5MXRra3FpcGRmcGt0Z2xlZTBvMW5tMDM1cTZ5ejJ1MnVxend2ciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Rjk1cMOdnjKxjoTHyf/giphy.gif",
    "home": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2xpZnFjb3EybWwyN2ZuanV2Z2NmdTZxamM4emVram0yajl4amZ6ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/UvWQ52x1XbJyJPmINe/giphy.gif",
    "family": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExajN3aTYwM3doeDU3cHd0emdiNzRqOXc0Y3oxbjJ2emY1bjQ2c3o5aSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKoGpYpK5Gct9gA/giphy.gif",
    "friend": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzN0bHR1b3dreWdmZzN0a3l4c3VhNjFpN2l5ZHBpM2lna29rdm80MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKxJ9b7iHDWj0pa/giphy.gif",
    "food": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExajR5ZDA1MmptcTA5cG1ydHZxMnFvOXFtb2tkcXBlcTZqZWJ3YXR0aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26DOtLVBDesaOnTJm/giphy.gif",
    "water": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzFyOG05ZzRnazNqaTM0OGxjOHBzNjZjZmxlMGU4enlhMW43NW51eSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26DOtNnaZuvgS5wTS/giphy.gif",
    "eat": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDJxYXY2MXRjZTdydjRoNGJwaHE4Z3NiemEydzY1NmZvN2ozejR0aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l3vRhFBHY2JT5QIdq/giphy.gif",
    "drink": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmRnNG5pMGcydTJwOW8xN2wzdWJ6eWV3aGR3bnRvZ3k1ZmU0NDNnZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/H1plpiFBFaTNstob0N/giphy.gif",
    "happy": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExczNxaGU4b2lmMHc2aHZoZmMwZjNqdzFpaGZreHF6czNhZmM3eW5tciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKFpahYpUp4g0N2/giphy.gif",
    "sad": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2ZpcTd6b3JkcmVvNWhwMW1hOXFnZHRwdjZ1bDJ1eXdwMnd5N2NoMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKVhsMTczdAzMB2/giphy.gif",
    "stop": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWJ2Z3Jzc3Z0ZHY1ZmMwYnZvdnVjY2Jmb3BvdndzMHB5eng1b3doNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oz8xvTLySRClnMMko/giphy.gif",
    "wait": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGV5dnE5dmJ6aTVjaGUzNGc4bnVycGdoc2hwZ2l6dDBjZGVjbzBndyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l0MYG8QvlyLRudjJS/giphy.gif",
    "nice": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTFvbGNrOGRnaHVhajU1cm11djk4bHltbG95aDljb21oNHM0N3MyYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XFij2pgqluInrq8OPg/giphy.gif",
    "meet": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2hobGc3aGR1azNxMDhuMThnYWswbnFva2gxamE1NGZlbWFyd2tkNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/RGjnL3w3ZZyf7rlcM0/giphy.gif",
}

