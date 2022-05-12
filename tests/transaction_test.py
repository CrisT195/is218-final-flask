def test_csv_upload(client): # , auth):
    # response1 = auth.register()
    # response3 = auth.login()
    csv = "tests/sample_transactions.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "sample_transactions.csv")}
    response2 = client.post("/transaction/upload", data=data)
    print(response2.data)
    # assert response2.status_code == 302
    # assert response2.headers["Location"] == "/transaction_datatables"


def test_transaction_balance(client): # , auth):
    # response1 = auth.register()
    # response2 = auth.login()
    csv = "tests/sample_transactions.csv"
    csv_data = open(csv, "rb")
    data = {"file": (csv_data, "sample_transactions.csv")}
    response4 = client.post("/transaction/upload", data=data)
    # assert response2.status_code == 302
    response3 = client.get("/transaction_datatables")
    # assert b"Current Balance:  $300.0" in response3.data
    # assert response3.status_code == 200


def test_transaction_pages(client):
    """This makes the index page"""
    response = client.get("/transaction_datatables")
    assert response.status_code == 302
    response = client.get("/transaction/upload")
    assert response.status_code == 302
