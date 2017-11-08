class Coord():
    x = 0
    y = 0
    z = 0


class Quat():
    x = 0
    y = 0
    z = 0
    w = 0


class Pose():
    position = Coord()
    orientation = Quat()


class Twist():
    linear = Coord()
    angular = Coord()


class State():
    model_name = ""
    pose = Pose()
    twist = Twist()
    reference_frame = "world"

    def __init__(self, model, position, orientation, linear, angular, ref):
        self.model_name = model
        self.reference_frame = ref

        self.pose.position.x, \
        self.pose.position.y, \
        self.pose.position.z = position

        self.pose.orientation.x, \
        self.pose.orientation.y, \
        self.pose.orientation.z, \
        self.pose.orientation.w = orientation

        self.twist.linear.x, \
        self.twist.linear.y, \
        self.twist.linear.z = linear

        self.twist.angular.x, \
        self.twist.angular.y, \
        self.twist.angular.z = angular
