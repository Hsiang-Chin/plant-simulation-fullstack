import socket

def start_server():
    # 設定 IP 與 Port (127.0.0.1 代表本機)
    HOST = '127.0.0.1'
    PORT = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server 已啟動，正在監聽 {HOST}:{PORT}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"已連接來自: {addr} 的客戶端")
        
        try:
            while True:
                # 接收從 PlantSimulation 傳來的資料
                data = conn.recv(1024)
                if not data:
                    break
                
                # 解碼並印出訊息
                message = data.decode('utf-8').strip()
                print(f"收到來自 PlantSim 的訊息: {message}")
                
                # 回傳確認訊息給 PlantSimulation
                response = f"Server 已收到訊息: [{message}]\r\n"
                conn.sendall(response.encode('utf-8'))
                
        except ConnectionResetError:
            print("客戶端強制斷開連線")
        finally:
            conn.close()
            print("連線已關閉，等待下一個連線...\n")

if __name__ == "__main__":
    start_server()