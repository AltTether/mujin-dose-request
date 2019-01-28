# mujin-dose-request
doseでの購入リクエストを保持するためのサーバ

## requirements  
docker  

## usage

1. Build image  
    ```
    docker build -t mujin-dose-request .  
    ```

1. Run container  
    ```
    docker run -it -v $(pwd):/app -p 5004:5000 mujin-dose-request  
    ```
