from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

from jinja2 import Environment, FileSystemLoader
def actual_main():
    # Step 6: Create MindMapComposite and MindMapLeaf objects to test
    root = MindMapComposite("Root", "circle")
    leaf1 = MindMapLeaf("Child 1", "square")
    leaf2 = MindMapLeaf("Child 2", "cloud")
    root.add(leaf1)
    root.add(leaf2)

    print(str(root))  # Should display "((Root))"
    root.display()  # Should display root and its children

    print("MindMapComposite tests completed!")

    root = MindMapComposite("The Battle at Wolf 359", "circle")

    characters = MindMapComposite("Characters", "oval")
    characters.add(MindMapLeaf("Jean-Luc Picard / Locutus", "plain"))
    characters.add(MindMapLeaf("William Riker", "plain"))
    characters.add(MindMapLeaf("Data", "plain"))
    characters.add(MindMapLeaf("Worf", "plain"))
    characters.add(MindMapLeaf("Borg Queen (implied presence)", "plain"))
    root.add(characters)

    plot_points = MindMapComposite("Plot Points", "square")
    plot_points.add(MindMapLeaf("Picard is assimilated by the Borg", "plain"))
    plot_points.add(MindMapLeaf("Riker takes command of the Enterprise", "plain"))
    plot_points.add(MindMapLeaf("The Federation fleet suffers heavy losses", "plain"))
    plot_points.add(MindMapLeaf("Enterprise crew devises a plan to stop the Borg", "plain"))
    root.add(plot_points)

    themes = MindMapComposite("Themes", "cloud")
    themes.add(MindMapLeaf("Identity and loss of self", "plain"))
    themes.add(MindMapLeaf("Duty and leadership", "plain"))
    themes.add(MindMapLeaf("Humanity vs. technology", "plain"))
    themes.add(MindMapLeaf("Collectivism vs. individuality", "plain"))
    root.add(themes)

    setting = MindMapComposite("Setting", "hexagon")
    setting.add(MindMapLeaf("USS Enterprise-D", "plain"))
    setting.add(MindMapLeaf("Wolf 359 (space battle location)", "plain"))
    setting.add(MindMapLeaf("Borg Cube", "plain"))
    setting.add(MindMapLeaf("Starfleet Command (background communication)", "plain"))
    root.add(setting)

    conflicts = MindMapComposite("Major Conflicts", "bang")
    conflicts.add(MindMapLeaf("Federation vs. Borg (existential threat)", "plain"))
    conflicts.add(MindMapLeaf("Riker's internal struggle as acting captain", "plain"))
    conflicts.add(MindMapLeaf("Enterprise's fight to save Picard from assimilation", "plain"))
    root.add(conflicts)

    dialogue = MindMapComposite("Dialogue Highlights", "oval")
    dialogue.add(MindMapLeaf("“I am Locutus of Borg. Resistance is futile.”", "plain"))
    dialogue.add(MindMapLeaf("Riker: \"Mr. Worf, fire.\"", "plain"))
    dialogue.add(MindMapLeaf("Guinan advising Riker on letting go of Picard", "plain"))
    root.add(dialogue)

    stage_directions = MindMapComposite("Significant Stage Directions", "square")
    stage_directions.add(MindMapLeaf("Close-up of Picard’s face as Locutus", "plain"))
    stage_directions.add(MindMapLeaf("Panoramic view of the devastated fleet at Wolf 359", "plain"))
    stage_directions.add(MindMapLeaf("Enterprise maneuvering to evade the Borg", "plain"))
    stage_directions.add(MindMapLeaf("Tense bridge scenes as the crew works together", "plain"))
    root.add(stage_directions)

    daniel_tiger = MindMapComposite("Daniel Tiger", "cloud")
    friends = MindMapComposite("Friends", "circle")
    phrases = MindMapComposite("Phrases", "hexagon")
    daniel_tiger.add(friends)
    daniel_tiger.add(phrases)
    phrases.add(MindMapLeaf("Grr iffic", ""))
    phrases.add(MindMapLeaf("Tiger tastic", ""))
    phrases.add(MindMapLeaf("this is not a quote", ""))

    friends.add(MindMapLeaf("Miss Elaina", "cloud"))
    friends.add(MindMapLeaf("Katerina Kittykat", "square"))
    friends.add(MindMapLeaf("Prince Wednesday", "cloud"))

    with open("mindmaps/daniel_tiger.html", "w",encoding="utf+8") as file:
        file.write(get_html_mindmap(daniel_tiger))

def get_html_mindmap(root):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("templates/jinja.j2")
    output = template.render(mindmap=root.get_str())
    return output



if __name__ == "__main__":
    actual_main()