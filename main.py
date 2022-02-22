class Car:
    def __init__(self, license_number):
        self.license_number = license_number


class ParkingSlot:
    def __init__(self, row, spot_number, level, car):
        self.row = row
        self.spot_number = spot_number
        self.level = level
        self.car = car

    def is_avaible(self):
        return self.car is None

    def park(self, vehicle):
        self.car = vehicle

    def remove_vehicle(self):
        self.car is None

class Level:
    def __init__(self, rows, level_number)
        self.rows = rows
        self.level_number = level_number
        self.spots_per_row = 2
        self.parking_slots = []
        self.available_slots = rows + self.spots_per_row

    def find_available_slot(self):
        if self.available_slots <= 0:
            return None
        else:
            if len(self.parking_slots) == 0:
                return ParkingSlot(0,0,0, None)
            else:
                last_car_parked = self.parking_slots[-1]

            if last_car_parked.spot_number < self.spots_per_row:
                return ParkingSlot(last_car_parked.row, last_car_parked.spot_number+1), self.level_number, None)
            if last_car_parked.row < self.row:
                return ParkingSlot(last_car_parked.row+1,0,self.level_number, None)



