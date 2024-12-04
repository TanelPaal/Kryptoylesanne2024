# Kryptoülesanne
Krüptograafia-alane kodutöö.<br>
Uni-ID: 222775IADB

## Project Description / Projekti Kirjeldus
[EN] This project involves finding collisions and preimages in a custom hash function called PRSHA-1, which is a reduced version of the SHA-1 hash function. The goal is to demonstrate the vulnerability of certain hash functions to collision and preimage attacks.<br>

[EE] See projekt hõlmab kokkupõrgete ja eelkujutiste leidmist kohandatud räsi funktsioonis nimega PRSHA-1, mis on SHA-1 räsi funktsiooni vähendatud versioon. Eesmärk on näidata teatud räsi funktsioonide haavatavust kokkupõrgete ja eelkujutiste rünnakute suhtes.

## Files / Failid
- `Collision.py`:[EN] Contains the implementation for finding collisions in the PRSHA-1 hash function.<br> [EE] Sisaldab kokkupõrgete leidmise PRSHA-1 räsi funktsiooni rakendust.
- `CollisionPreimage.py`: [EN] Contains the implementation for finding preimages in the PRSHA-1 hash function.<br> [EE] Sisaldab eelkujutiste leidmise PRSHA-1 räsi funktsiooni rakendust.

## How to Run / Kuidas Käivitada
1. [EN] Ensure you have Python installed on your system.<br> [EE] Veenduge, et teie süsteemis oleks installitud Python.
2. [EN] Run the `Collision.py` script to find collisions.<br> [EE] Käivitage `Collision.py` skript kokkupõrgete leidmiseks:
    ```sh
    python Collision.py
    ```
3. [EN] Run the `CollisionPreimage.py` script to find preimages.<br> [EE] Käivitage `CollisionPreimage.py` skript eelkujutiste leidmiseks:
    ```sh
    python CollisionPreimage.py
    ```
