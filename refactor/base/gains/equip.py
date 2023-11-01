from base.status import Status


def manufacture_set_critical_11300(status: Status):
    status.attribute.all_critical_strike_base += 1090


def manufacture_set_strain_11300(status: Status):
    status.attribute.strain_base += 1090


def manufacture_set_critical_12600(status: Status):
    status.attribute.all_critical_strike_base += 1215


def manufacture_set_strain_12600(status: Status):
    status.attribute.strain_base += 1215


def manufacture_set_critical_14150(status: Status):
    status.attribute.all_critical_strike_base += 1363


def manufacture_set_strain_14150(status: Status):
    status.attribute.strain_base += 1363
