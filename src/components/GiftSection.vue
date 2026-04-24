<template>
 <section class="py-24 bg-surface relative overflow-hidden">
 <div class="max-w-4xl mx-auto px-6 text-center">
 <!-- Section Header -->
 <div class="mb-16 space-y-4">
 <div class="inline-block p-3 rounded-full bg-primary/10 text-primary mb-4">
 <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-gift"><polyline points="20 12 20 22 4 22 4 12"></polyline><rect x="2" y="7" width="20" height="5"></rect><line x1="12" y1="22" x2="12" y2="7"></line><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path></svg>
 </div>
 <h3 class="text-4xl font-serif text-on-surface">Digital Gift</h3>
 <p class="text-on-surface/60 font-sans max-w-lg mx-auto">
 Your presence is the greatest gift of all. However, if you wish to honor us with a gift, a digital contribution would be very much appreciated.
 </p>
 </div>

 <!-- Bank Cards -->
 <div class="grid md:grid-cols-2 gap-8 mt-12">
 <div 
 v-for="(account, index) in bankAccounts" 
 :key="index"
 class="glass-panel p-8 rounded-3xl p-8 relative overflow-hidden group hover:border-primary/50 transition-all duration-500"
 >
 <!-- Card Decorative Gradient -->
 <div class="absolute -top-10 -right-10 w-32 h-32 bg-primary/10 rounded-full blur-2xl group-hover:bg-primary-container hover:text-on-primary-container/20 transition-all duration-700"></div>
 
 <div class="relative z-10 flex flex-col items-center">
 <div class="text-xs tracking-[0.3em] uppercase text-primary/70 mb-2">{{ account.bankName }}</div>
 <div class="text-2xl font-sans font-semibold text-on-surface tracking-wider mb-1">{{ account.accountNumber }}</div>
 <div class="text-sm font-sans text-on-surface/50 mb-6">a/n {{ account.accountName }}</div>
 
 <button 
 @click="copyNumber(account.accountNumber, index)"
 class="px-6 py-2 rounded-full border border-primary/30 text-primary text-xs uppercase tracking-widest hover:bg-primary-container hover:text-on-primary-container hover:text-on-surface transition-all duration-300"
 >
 {{ copiedIndex === index ? 'Copied!' : 'Copy Number' }}
 </button>
 </div>
 </div>
 </div>
 </div>
 </section>
</template>

<script setup>
import { ref } from 'vue';

const bankAccounts = [
 {
 bankName: 'Bank Central Asia (BCA)',
 accountNumber: '1234567890',
 accountName: 'Romeo Montague'
 },
 {
 bankName: 'Bank Mandiri',
 accountNumber: '0987654321',
 accountName: 'Juliet Capulet'
 }
];

const copiedIndex = ref(null);

const copyNumber = (number, index) => {
 navigator.clipboard.writeText(number).then(() => {
 copiedIndex.value = index;
 setTimeout(() => {
 copiedIndex.value = null;
 }, 2000);
 });
};
</script>

<style scoped>
.glass-panel {
 background: rgba(255, 255, 255, 0.4);
 backdrop-filter: blur(12px);
 border: 1px solid rgba(212, 175, 55, 0.1);
}
</style>
