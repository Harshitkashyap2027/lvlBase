// lvlBase WebRTC Utilities for Battle & Proctoring
const WebRTCManager = {
  peerConnection: null,
  localStream: null,
  remoteStream: null,
  
  config: {
    iceServers: [
      { urls: 'stun:stun.l.google.com:19302' },
      { urls: 'stun:stun1.l.google.com:19302' }
    ]
  },
  
  async getMedia(video = true, audio = true) {
    try {
      this.localStream = await navigator.mediaDevices.getUserMedia({ video, audio });
      return this.localStream;
    } catch (err) {
      console.error('Media access denied:', err);
      throw err;
    }
  },
  
  async createPeerConnection(onIceCandidate, onTrack) {
    this.peerConnection = new RTCPeerConnection(this.config);
    
    this.peerConnection.onicecandidate = (e) => {
      if (e.candidate) onIceCandidate(e.candidate);
    };
    
    this.peerConnection.ontrack = (e) => {
      this.remoteStream = e.streams[0];
      onTrack(this.remoteStream);
    };
    
    if (this.localStream) {
      this.localStream.getTracks().forEach(track => {
        this.peerConnection.addTrack(track, this.localStream);
      });
    }
    
    return this.peerConnection;
  },
  
  async createOffer() {
    const offer = await this.peerConnection.createOffer();
    await this.peerConnection.setLocalDescription(offer);
    return offer;
  },
  
  async createAnswer(offer) {
    await this.peerConnection.setRemoteDescription(new RTCSessionDescription(offer));
    const answer = await this.peerConnection.createAnswer();
    await this.peerConnection.setLocalDescription(answer);
    return answer;
  },
  
  async addAnswer(answer) {
    await this.peerConnection.setRemoteDescription(new RTCSessionDescription(answer));
  },
  
  addIceCandidate(candidate) {
    this.peerConnection?.addIceCandidate(new RTCIceCandidate(candidate));
  },
  
  disconnect() {
    this.localStream?.getTracks().forEach(t => t.stop());
    this.peerConnection?.close();
    this.peerConnection = null;
    this.localStream = null;
    this.remoteStream = null;
  }
};

export default WebRTCManager;
