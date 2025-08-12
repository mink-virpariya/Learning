from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
        Cricket is more than just a sport; it is a blend of skill, strategy, patience, and passion that has captured the hearts of millions around the world. Played between two teams of eleven players each, it revolves around batting, bowling, and fielding, but within that simple framework lies a rich complexity. A cricket match begins with the toss of a coin, where the winning captain decides whether to bat or bowl first. The batting side aims to score as many runs as possible, while the bowling and fielding side works to dismiss the batsmen and restrict the score. Bowlers employ a variety of deliveries—pace, swing, seam, and spin—each designed to outwit the batter. Batters, in turn, rely on timing, placement, and footwork to negotiate the ball and find gaps in the field. Fielders play a crucial role, diving, sprinting, and catching to save runs or claim wickets. Cricket is played in several formats: Test cricket, the traditional five-day game; One Day Internationals (ODIs), limited to 50 overs per side; and the fast-paced Twenty20 (T20) format, with just 20 overs per side. Each format brings its own style and tempo, from the patient endurance of Tests to the explosive hitting of T20s. Beyond the technicalities, cricket is celebrated for its spirit of sportsmanship, famously referred to as “the gentleman’s game.” Matches often create unforgettable moments—last-ball finishes, record-breaking innings, and displays of extraordinary athleticism—that live on in fans’ memories. In many countries, especially India, England, Australia, Pakistan, and the West Indies, cricket is deeply intertwined with culture and national pride. It is not uncommon for streets to fall silent when a high-stakes match is underway, uniting people across backgrounds. Ultimately, cricket is a game of moments—both grand and subtle—that reflect teamwork, resilience, and the timeless joy of competition.

    """

splitter = RecursiveCharacterTextSplitter(chunk_size=100,
                                 chunk_overlap=0,
                                 )

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)
