import yaml


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

    @staticmethod
    def make(model, position, orientation, linear, angular, ref):
        s = State()
        s.model_name = model
        s.reference_frame = ref

        s.pose.position.x, \
        s.pose.position.y, \
        s.pose.position.z = position

        s.pose.orientation.x, \
        s.pose.orientation.y, \
        s.pose.orientation.z, \
        s.pose.orientation.w = orientation

        s.twist.linear.x, \
        s.twist.linear.y, \
        s.twist.linear.z = linear

        s.twist.angular.x, \
        s.twist.angular.y, \
        s.twist.angular.z = angular

        return s

    @staticmethod
    def from_get_state(data, model, ref):
        s = State()
        s.model_name = model
        s.reference_frame = ref
        s.pose = data.pose
        s.twist = data.twist

        return s

    def __str__(self):
        return (
            "model_name: {}\n"
            "pose:\n{}\n"
            "twist:\n{}\n"
            "reference_frame: {}".format(
                self.model_name,
                self.pose,
                self.twist,
                self.reference_frame
            )
        )
