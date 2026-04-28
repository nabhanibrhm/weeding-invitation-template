<template>
 <div 
 class="fixed bottom-6 left-6 z-[60] transition-all duration-700"
 :class="isVisible ? 'translate-y-0 opacity-100' : 'translate-y-20 opacity-0'"
 >
 <button 
 @click="toggleMusic"
 class="relative group"
 aria-label="Toggle Music"
 >
 <!-- Pulse Effect -->
 <div 
 v-if="isPlaying"
 class="absolute inset-0 bg-primary/30 rounded-full animate-ping scale-150"
 ></div>
 
 <!-- Button Body -->
 <div 
 class="relative flex items-center justify-center w-12 h-12 rounded-full border border-primary/30 glass-panel hover:border-primary transition-all duration-300"
 :class="isPlaying ? 'rotate-animation' : ''"
 >
 <svg v-if="isPlaying" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-black">
 <path d="M9 18V5l12-2v13"></path>
 <circle cx="6" cy="18" r="3"></circle>
 <circle cx="18" cy="16" r="3"></circle>
 </svg>
 <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-on-surface/50">
 <line x1="1" y1="1" x2="23" y2="23"></line>
 <path d="M9 18V5l12-2v13"></path>
 <circle cx="6" cy="18" r="3"></circle>
 <circle cx="18" cy="16" r="3"></circle>
 </svg>
 </div>

 <!-- Tooltip -->
 <span class="absolute left-16 top-1/2 -translate-y-1/2 px-3 py-1 bg-primary text-on-primary rounded-lg text-black text-[10px] tracking-widest uppercase rounded opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none whitespace-nowrap">
 {{ isPlaying ? 'Mute' : 'Play' }} Music
 </span>
 </button>
 </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';

const props = defineProps({
 audioRef: {
 type: Object,
 default: null
 },
 isVisible: {
 type: Boolean,
 default: false
 }
});

const isPlaying = ref(false);

const toggleMusic = () => {
 if (!props.audioRef) return;
 
 if (props.audioRef.paused) {
 props.audioRef.play().catch(e => console.error('Audio play failed:', e));
 isPlaying.value = true;
 } else {
 props.audioRef.pause();
 isPlaying.value = false;
 }
};

// Sync internal state if audio is played from elsewhere (like the shutter button)
onMounted(() => {
 if (props.audioRef) {
 isPlaying.value = !props.audioRef.paused;
 
 // Listen for outside play events
 props.audioRef.onplay = () => isPlaying.value = true;
 props.audioRef.onpause = () => isPlaying.value = false;
 }
});

watch(() => props.isVisible, (newVal) => {
 if (newVal && props.audioRef) {
 isPlaying.value = !props.audioRef.paused;
 }
});
</script>

<style scoped>
.rotate-animation {
 animation: rotate 8s linear infinite;
}

@keyframes rotate {
 from { transform: rotate(0deg); }
 to { transform: rotate(360deg); }
}

.glass-panel {
 background: rgba(255, 255, 255, 0.05);
 backdrop-filter: blur(8px);
}
</style>
