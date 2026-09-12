import pickle

class ExperimentSnapshot:
    def __init__(self, experiment_id, model_type, hyperparameters, metrics, timestamp):
        self.experiment_id = experiment_id
        self.model_type = model_type
        self.hyperparameters = hyperparameters
        self.metrics = metrics
        self.timestamp = timestamp

    def get_best_metric(self, metric_name):
        return self.metrics[metric_name]

def save_experiment(snapshot, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(snapshot, f)

def load_experiment(file_path):

    with open(file_path, "rb") as f:
        return pickle.load(f)

def main():
    exp = ExperimentSnapshot(
        "EXP-2026-001",
        "RandomForest",
        {"n_estimators": 100, "max_depth": 10},
        {"accuracy": 0.942, "f1_score": 0.938},
        "2026-09-01 10:00:00"
    )
    save_experiment(exp, "experiment_01.pkl")
    restored_exp = load_experiment("experiment_01.pkl")
    print(restored_exp.model_type)
    print(restored_exp.get_best_metric("accuracy"))

main()