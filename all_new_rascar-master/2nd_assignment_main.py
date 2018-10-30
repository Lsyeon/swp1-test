#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def __init__(self,channel):
	GPIO.setmode(GPIO.BOARD)
	self.gpio_channel = channel

	for i in range(0, 5):
            GPIO.setup(self.gpio_channel[i], GPIO.IN)
    def read_digital(self):	#트랙의 검정색 라인 부분을 감지하는 메소드
        digital_list = []	#검정색 라인을 감지한 정보를 저장
        for i in range(0, 5):
            temp = GPIO.input(self.gpio_channel[i])	#5개 5번
            digital_list.append(0 if temp == 1 else 1)
        return digital_list	#색저장

    def is_in_line(self):	#검정색라인 탐지 메소드
        lt_status = self.read_digital()
        if 1 in lt_status:
            return True		#즉 검정색라인(1) 이면 True 1이 없으면 false 
        else:
            return False

    def is_equal_status(self, status):
        lt_status = self.read_digital()	#센서값 읽기
        if lt_status == status:
            return True
        else:
            return False
	#if(is_equal_status([0,0,1,0,0]):
		#back.forward_with_speed(90) 구동체를 90의 속도로 후진한다

    def is_center(self):
        lt_status = self.read_digital()
        if lt_status[2] == 1:
            return True
        else:
            return False

    def car_startup(self):
        self.car.accelerator.go_forward(15)
	while True:
	    l = self.car.line_detector.read_digital()
	    if l == [1, 1, 0, 0, 0]:
		self.car.steering.turn_right(30)
	    elif l == [0, 1, 1, 0, 0]:
		self.car.steering.turn_right(10)
	    elif l == [0, 0, 1, 1, 0 ]:
		self.car.steering.turn_left(10)
	    elif l == [0, 0, 0, 1, 1]:
		self.car.steering.turn_left(30)
	    elif l ==[1, 0, 0, 0, 0]:
		self.car.steering.turn_right(35)
	    elif l == [0, 0, 0, 0, 1]:
		self.car.steering.turn_left(35)
	    elif l == [1, 1, 1, 1, 1]:
		self.car.accelerator.stop()
	    time.sleep(0,1)

        pass


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
