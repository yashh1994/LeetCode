class MyCalendarTwo:

    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for b in self.double_bookings:
            if not (end <= b[0] or start >= b[1]):
                return False
        
        for b in self.single_bookings:
            if not (end <= b[0] or start >= b[1]):
                overlap_start = max(start, b[0])
                overlap_end = min(end, b[1])
                self.double_bookings.append((overlap_start, overlap_end))
        
        self.single_bookings.append((start, end))
        return True
