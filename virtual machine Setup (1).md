### virtual machine Setup Troubleshooting

# Simulating GPU Clustering Using CPU with KVM and Kubernetes

1. **Install KVM and Dependencies**:
   ```
   sudo apt update
   sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
   sudo systemctl enable libvirtd
   sudo systemctl start libvirtd
   ```

2. **Check If KVM is Working**:
   ```
   egrep -c '(vmx|svm)' /proc/cpuinfo
   ```

3. **Add Yourself to the `libvirt` and `kvm` Groups**:
   ```
   sudo usermod -aG libvirt,kvm $USER
   ```


1. **Install Virt-Manager**:
   ```
   sudo apt install virt-manager
   ```

2. **Create Virtual Machines**:
   - Open `virt-manager` and create VMs with **1 CPU** and at least **1 GB of RAM** using Ubuntu Server.
   - Name them `gpu-node-1`, `gpu-node-2`, etc.


1. **SSH into Each VM**:
   ```
   ssh user@gpu-node-1
   ```

2. **Install Docker**:
   ```
   sudo apt update
   sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   sudo apt update
   sudo apt install -y docker-ce
   sudo systemctl enable docker

```bash
sudo usermod -aG docker $USER
newgrp docker
```
This will allow your user to access the Docker daemon without needing `sudo`.

Kubernetes packages (`kubectl`, `kubeadm`, `kubelet`)  installation.
epository is missing or incorrectly added. You can add it using the following steps:
1. **Add Google Cloud Apt Key:**
   ```bash
   curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
   ```
2. **Add the Kubernetes Repository:**
   ```bash
   echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
   ```
3. **Update Package List and Install:**
   ```bash
   sudo apt-get update
   sudo apt-get install -y kubelet kubeadm kubectl
   ```
 Installing `KVM` or `VirtualBox` if you prefer not to use Docker as the driver.

Running `kubeadm join` results in a DNS resolution failure.
```bash
sudo nano /etc/hosts
<MINIKUBE_IP> control-plane.minikube.internal
```
Replace `<MINIKUBE_IP>` with the IP address returned by `minikube ip`.

`kubelet` service is missing and cannot be enabled.

 **Remove Snap Version of Kubelet** (if installed):
   ```bash
   sudo snap remove kubelet
   ```
**Install Kubernetes 
   Add the official Kubernetes repository, then update and install `kubelet`, `kubeadm`, and `kubectl`:
   ```bash
   curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
   echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
   sudo apt-get update
   sudo apt-get install -y kubelet kubeadm kubectl
   sudo systemctl enable kubelet
   sudo systemctl start kubelet
   ```

Minikube status shows that it cannot connect to libvirt socket.
```bash
sudo usermod -aG libvirt $USER
newgrp libvirt
```
Then restart Minikube:
```bash
minikube stop
minikube start --driver=kvm2
```
error generation while generating the minikube with kvm
working on the error

