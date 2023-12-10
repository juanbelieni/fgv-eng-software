import pytest
from utils.notification import NotificationObserver


@pytest.fixture
def notification_observer():
    return NotificationObserver()


def test_subscribe(notification_observer):
    def dummy_callback(message):
        pass

    notification_observer.subscribe("success", dummy_callback)
    assert len(notification_observer.subscribers["success"]) == 1


def test_unsubscribe(notification_observer):
    def dummy_callback(message):
        pass

    notification_observer.subscribe("success", dummy_callback)
    notification_observer.unsubscribe("success", dummy_callback)
    assert len(notification_observer.subscribers["success"]) == 0


def test_notify(notification_observer, capsys):
    def dummy_callback(message):
        print(message)

    notification_observer.subscribe("success", dummy_callback)
    notification_observer.notify("success", "Test Message")

    captured = capsys.readouterr()
    assert "Test Message" in captured.out
