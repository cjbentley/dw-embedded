def control_law(array):
	motor_L = 0
	motor_R = 0

	LS_X = float(array[0])
	LS_Y = array[1]
	RS_X = array[2]
	RS_Y = array[3]
	LT = array[4]
	RT = array[5]
	DPAD = array[6]
	A = array[7]
	B = array[8]
	X = array[9]
	Y = array[10]
	LB = array[11]
	RB = array[12]
	LS_B = array[13]
	RS_B = array[14]
	SELECT = array[15]

	# 0 = forward motion, 1 = spot steer
	mode = 0

	# Mapping
	LT = int(round(100*float(LT), 0))
	RT = int(round(100*float(RT), 0))

	if LT == 0 and RT == 0:
		mode = 1

	if mode == 1: # Spot steer
		percent = int(round((abs(LS_X)/0.5)*100, 0))
		if float(LS_X) < 0: # LEFT
			motor_L = -percent
			motor_R = percent
		elif float(LS_X) > 0: # RIGHT
			motor_L = percent
			motor_R = -percent
	
	elif mode == 0:
		percent = 0
		if LT > RT:
			percent = -LT
		else:
			percent = RT

		motor_L = percent - abs(LS_X)
		motor_R = percent + abs(LS_X)
		print(motor_L, motor_R)