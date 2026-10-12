import app as appmodule

class FakeRedis:
    def __init__(self):
        self.n = 0
    def incr(self, key):
        self.n += 1
        return self.n

def test_home(monkeypatch):
    monkeypatch.setattr(appmodule, "cache", FakeRedis())
    client = appmodule.app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert "1 fois" in r.get_data(as_text=True)
