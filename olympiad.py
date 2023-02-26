class Olympiad:
    def __init__(
                 self,
                 subject_names,
                 olympiad_name,
                 classes,
                 date,
                 ref_to_organizer,
                 ref_to_registration,
                 tasks,
                 level
                ):
        self.subject_names = subject_names
        self.name = olympiad_name
        self.classes = classes
        self.date = date
        self.ref_to_organizer = ref_to_organizer
        self.ref_to_registration = ref_to_registration
        self.tasks = tasks
        self.level = level
