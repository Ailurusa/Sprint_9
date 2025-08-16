from faker import Faker

fake = Faker()


def get_fake_email():
    return fake.email()


def get_fake_password():
    return fake.password(length=8)


def get_fake_username():
    return fake.unique.user_name()


def get_fake_first_name():
    return fake.first_name()


def get_fake_last_name():
    return fake.last_name()
