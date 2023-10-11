import json

class MedicinalPlantsApp:
    def __init__(self):
        self.plants_data = {}
        self.admin_password = "your_secure_password"  # Set your admin password here

    def load_data(self, data_file):
        try:
            with open(data_file, 'r') as file:
                self.plants_data = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("Data file not found. Creating a new database.")
            self.plants_data = {}

    def save_data(self, data_file):
        with open(data_file, 'w') as file:
            json.dump(self.plants_data, file)
        print("Data saved successfully.")

    def add_plant(self, name, description, properties, password):
        if password == self.admin_password:
            if name not in self.plants_data:
                self.plants_data[name] = {
                    'description': description,
                    'properties': properties
                }
                print(f"{name} has been added to the database.")
            else:
                print(f"{name} already exists in the database.")
        else:
            print("Incorrect password. Access denied.")

    def get_plant_info(self, name):
        if name in self.plants_data:
            plant_info = self.plants_data[name]
            print(f"Name: {name}")
            print(f"Description: {plant_info['description']}")
            print("Properties:")
            for prop in plant_info['properties']:
                print(f"- {prop}")
        else:
            print(f"{name} not found in the database.")

    def list_plants(self):
        print("List of Medicinal Plants:")
        for name in self.plants_data:
            print(name)

if __name__ == "__main__":
    app = MedicinalPlantsApp()
    data_file = "medicinal_plants_data.json"

    app.load_data(data_file)

    medicinal_plants = {
        "Aloe Vera": {
            'description': "Aloe vera is known for its soothing and healing properties.",
            'properties': ["Anti-inflammatory", "Skin healing"]
        },
        "Turmeric": {
            'description': "Turmeric is a powerful anti-inflammatory and antioxidant spice.",
            'properties': ["Anti-inflammatory", "Antioxidant", "Immune-boosting"]
        },
        "Lavender": {
            'description': "Lavender is used for its calming and relaxing effects.",
            'properties': ["Stress relief", "Sleep aid"]
        },
        "Garlic": {
            'description': "Garlic is a natural antibiotic and immune system booster.",
            'properties': ["Antibiotic", "Immune-boosting"]
        },
        "Ginger": {
            'description': "Ginger is known for its anti-nausea and anti-inflammatory properties.",
            'properties': ["Anti-nausea", "Anti-inflammatory"]
        },
        "Peppermint": {
            'description': "Peppermint is used for digestive and respiratory conditions.",
            'properties': ["Digestive aid", "Respiratory relief"]
        },
        "Echinacea": {
            'description': "Echinacea is a popular herbal remedy for colds and infections.",
            'properties': ["Immune-boosting", "Cold remedy"]
        },
        "Chamomile": {
            'description': "Chamomile is known for its calming and sleep-inducing effects.",
            'properties': ["Sleep aid", "Stress relief"]
        },
        "Oregano": {
            'description': "Oregano is a powerful herb with antibacterial properties.",
            'properties': ["Antibacterial", "Antioxidant"]
        },
        "Thyme": {
            'description': "Thyme is used for respiratory and culinary purposes.",
            'properties': ["Respiratory aid", "Culinary herb"]
        },
        "Lemon Balm": {
            'description': "Lemon balm is known for its calming and mood-enhancing properties.",
            'properties': ["Calming", "Mood-enhancing"]
        },
        "Ginseng": {
            'description': "Ginseng is an adaptogen known for its energy-boosting properties.",
            'properties': ["Energy-boosting", "Adaptogen"]
        },
        "Valerian": {
            'description': "Valerian is used for its sedative and sleep-promoting effects.",
            'properties': ["Sedative", "Sleep aid"]
        },
        "Milk Thistle": {
            'description': "Milk thistle is known for its liver-protective properties.",
            'properties': ["Liver-protective", "Detoxification"]
        },
        "St. John's Wort": {
            'description': "St. John's Wort is used as a natural antidepressant.",
            'properties': ["Antidepressant", "Mood enhancement"]
        },
        "Sage": {
            'description': "Sage is used for its antimicrobial and culinary properties.",
            'properties': ["Antimicrobial", "Culinary herb"]
        },
        "Rosemary": {
            'description': "Rosemary is a fragrant herb known for its culinary and cognitive-enhancing properties.",
            'properties': ["Cognitive enhancement", "Culinary herb"]
        },
        "Ginkgo Biloba": {
            'description': "Ginkgo biloba is known for its memory-enhancing properties.",
            'properties': ["Memory enhancement", "Cognitive support"]
        },
        "Eucalyptus": {
            'description': "Eucalyptus is used for its respiratory and aromatic properties.",
            'properties': ["Respiratory aid", "Aromatic"]
        },
        "Hawthorn": {
            'description': "Hawthorn is known for its heart-protective properties.",
            'properties': ["Heart-protective", "Cardiovascular support"]
        },
        "Chia Seeds": {
            'description': "Chia seeds are known for their nutritional and omega-3 fatty acid properties.",
            'properties': ["Nutritional", "Omega-3 fatty acids"]
        },
        "Neem": {
            'description': "Neem is used for its anti-bacterial and skin-healing properties.",
            'properties': ["Antibacterial", "Skin healing"]
        },
        "Dandelion": {
            'description': "Dandelion is used for its detoxifying and digestive properties.",
            'properties': ["Detoxifying", "Digestive aid"]
        },
        "Comfrey": {
            'description': "Comfrey is known for its wound-healing properties.",
            'properties': ["Wound healing", "Anti-inflammatory"]
        },
        "Burdock": {
            'description': "Burdock is used for its blood-purifying and anti-inflammatory properties.",
            'properties': ["Blood purifying", "Anti-inflammatory"]
        },
        "Arnica": {
            'description': "Arnica is used for its anti-inflammatory and pain-relief properties.",
            'properties': ["Anti-inflammatory", "Pain relief"]
        },
        "Calendula": {
            'description': "Calendula is known for its skin-soothing and anti-inflammatory properties.",
            'properties': ["Skin soothing", "Anti-inflammatory"]
        },
        "Mullein": {
            'description': "Mullein is used for its respiratory and calming properties.",
            'properties': ["Respiratory aid", "Calming"]
        },
        "Saw Palmetto": {
            'description': "Saw Palmetto is known for its prostate health properties.",
            'properties': ["Prostate health", "Hormonal balance"]
        },
        "Fenugreek": {
            'description': "Fenugreek is used for its digestive and lactation properties.",
            'properties': ["Digestive aid", "Lactation support"]
        },
        # Add more medicinal plants here...
    }

    for plant, info in medicinal_plants.items():
        app.add_plant(plant, info['description'], info['properties'], app.admin_password)

    while True:
        print("\nMedicinal Plants Awareness Application")
        print("1. Add Plant")
        print("2. Get Plant Info")
        print("3. List Plants")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            password = input("Enter admin password: ")
            name = input("Enter plant name: ")
            description = input("Enter plant description: ")
            properties = input("Enter plant properties (comma-separated): ").split(',')
            app.add_plant(name, description, properties, password)
        elif choice == '2':
            name = input("Enter plant name: ")
            app.get_plant_info(name)
        elif choice == '3':
            app.list_plants()
        elif choice == '4':
            app.save_data(data_file)
            print("Exiting Medicinal Plants Awareness Application. Data saved.")
            break
        else:
            print("Invalid choice. Please try again.")
