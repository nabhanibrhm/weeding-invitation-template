<template>
 <section class="py-24 bg-[#C08552] relative overflow-hidden">
 <div class="max-w-7xl mx-auto px-6">
 <!-- Section Header -->
 <div class="text-center mb-16 space-y-4">
 <h2 class="text-black text-sm tracking-[0.4em] uppercase font-sans">Our Moments</h2>
 <h3 class="text-4xl md:text-5xl font-serif text-on-surface">Photo Gallery</h3>
 </div>

 <!-- Masonry Grid -->
 <div class="grid grid-cols-2 md:grid-cols-3 gap-4" ref="galleryRef">
 <div 
 v-for="(image, index) in galleryImages" 
 :key="index"
 class="gallery-item opacity-0 translate-y-10 transition-all duration-700 ease-out h-full"
 :style="{ transitionDelay: `${index * 150}ms` }"
 :class="{'md:row-span-2': index % 4 === 1, 'row-span-1': index % 4 !== 1}"
 >
 <div class="w-full h-full overflow-hidden rounded group cursor-pointer aspect-[3/4]">
 <img 
 :src="image" 
 alt="Wedding Moment" 
 class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110 grayscale-[30%] group-hover:grayscale-0"
 loading="lazy"
 />
 <div class="absolute inset-0 bg-primary text-on-primary rounded-lg/40 opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex items-center justify-center">
 <div class="w-10 h-10 border border-white/50 rounded-full flex items-center justify-center">
 <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
 </div>
 </div>
 </div>
 </div>
 </div>
 </div>
 
 <!-- Decorative background elements -->
 <div class="absolute -top-24 -left-24 w-96 h-96 bg-primary/5 rounded-full blur-[100px]"></div>
 <div class="absolute -bottom-24 -right-24 w-96 h-96 bg-primary/5 rounded-full blur-[100px]"></div>
 </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const galleryRef = ref(null);

const galleryImages = [
 'https://images.unsplash.com/photo-1511795409834-ef04bbd61622?q=80&w=2069&auto=format&fit=crop',
 'https://images.unsplash.com/photo-1519741497674-611481863552?q=80&w=2070&auto=format&fit=crop',
 'https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?q=80&w=2070&auto=format&fit=crop',
 'https://images.unsplash.com/photo-1583939003579-730e3918a45a?q=80&w=1974&auto=format&fit=crop',
 'https://images.unsplash.com/photo-1469334031218-e382a71b716b?q=80&w=2070&auto=format&fit=crop',
 'https://images.unsplash.com/photo-1519225421980-715cb0215aed?q=80&w=2070&auto=format&fit=crop'
];

onMounted(() => {
 const observer = new IntersectionObserver((entries) => {
 if (entries[0].isIntersecting) {
 const items = galleryRef.value.querySelectorAll('.gallery-item');
 items.forEach(item => {
 item.classList.remove('opacity-0', 'translate-y-10');
 item.classList.add('opacity-100', 'translate-y-0');
 });
 }
 }, { threshold: 0.1 });

 if (galleryRef.value) {
 observer.observe(galleryRef.value);
 }
});
</script>

<style scoped>
.aspect-\[3\/4\] {
 aspect-ratio: 3/4;
}
</style>
