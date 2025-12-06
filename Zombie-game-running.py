import Game_Functionalities as gf

def display_intro():
    """AI generatod slop for intro text"""
    intro_text = """
        In a world overrun by the undead, humanity's last hope lies in your hands.
        As a fearless survivor, you must navigate through treacherous landscapes,
        scavenge for supplies, and fend off relentless zombie hordes.
        
        Your mission: to find a rumored safe haven where survivors are regrouping.
        Every decision you make could mean the difference between life and death.
        
        Are you ready to face the apocalypse and save what's left of humanity?
        The adventure begins now...
        """
    gf.typewriter_effect(intro_text, delay=0.03)



