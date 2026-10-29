declare function require(nome: string): any;

const fs = require('fs');
const entrada: string = fs.readFileSync(0, 'utf8');
const linhas: string[] = entrada.split(/\r?\n/);

// Escreva a sua solução aqui. Use console.log() para a saída.
export {};
