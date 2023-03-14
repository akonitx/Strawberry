class Car:
    def __init__(self, car_name) -> None:
        self.carname = car_name

    def __str__(self) -> str:
        return self.carname


suzuki = Car("suzuki")
print(suzuki.__str__())
