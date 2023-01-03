class Olympiad:
    def __init__(
                 self,
                 subject_name,
                 olympiad_name,
                 date,
                 ref_to_organizer,
                 ref_to_registration,
                 tasks,
                 level
                ):
        self.subject_name = subject_name
        self.name = olympiad_name
        self.date = date
        self.ref_to_organizer = ref_to_organizer
        self.ref_to_registration = ref_to_registration
        self.tasks = tasks
        self.level = level