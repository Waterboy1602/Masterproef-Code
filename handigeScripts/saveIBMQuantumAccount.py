from qiskit_ibm_runtime import QiskitRuntimeService
from dotenv import load_dotenv
import os

load_dotenv()

# Save an IBM Quantum account.
QiskitRuntimeService.save_account(channel="ibm_quantum", token=os.environ['IBM_TOKEN'], overwrite=True)