class Project:
    def __init__(self, name, description,license , authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        Authors = f"\nAuthors:"
        for i in self.authors:
            Authors += f"\n  - {i}" 
        
        Dependencies = f"\nDependencies:"
        for i in self.dependencies:
            Dependencies += f"\n  - {i}"
        
        Dev_dependencies = f"\nDevelopment dependencies"
        for i in self.dev_dependencies:
            Dev_dependencies += f"\n  - {i}"

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n{Authors}"
            f"\n{Dependencies} "
            f"\n{Dev_dependencies}"
        )
