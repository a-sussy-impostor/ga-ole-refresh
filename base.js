import { match } from './typeChart.js'

class Disk {
  constructor(name, type, number, bst, move, star, energy, special, mega, z, fuse) {
    this.name = name;
    this.type = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"].indexOf(type);
    this.number = number;
    this.bst = bst;
    this.move = [move[0], ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"].indexOf(move[1]), move[2], move[3]]; // [name, type, power, ps] // PS = P/S/N
    this.star = star;
    this.energy = energy;
    this.special = special;
    this.mega = mega;
    this.level = this.energy / 30; // hidden
    this.z = ["Breakneck Blitz", "All-Out Pummeling", "Supersonic Skystrike", "Acid Downpour", "Tectonic Rage", "Continental Crush", "Savage Spin-Out", "Never-Ending Nightmare", "Corkscrew Crash", "Inferno Overdrive", "Hydro Vortex", "Bloom Doom", "Gigavolt Havoc", "Shattered Psyche", "Subzero Slammer", "Devastating Drake", "Black Hole Eclipse", "Twinkle Tackle", "Catastropika", "Sinister Arrow Raid", "Malicious Moonsault", "Oceanic Operetta", "Guardian of Alola", "Soul-Stealing 7-Star Strike", "Stoked Sparksurfer", "Pulverizing Pancake", "Extreme Evoboost", "Genesis Supernova", "10,000,000 Volt Thunderbolt", "Light That Burns the Sky", "Searing Sunraze Smash", "Menacing Moonraze Maelstrom", "Let's Snuggle Forever", "Splintered Stormshards", "Clangorous Soulblaze"].indexOf(z);
    this.fuse = fuse; // list
  }

  Attack(enemy, selfch = [1, 1, 1, 1, 1], enemych = [1, 1, 1, 1, 1]) { // Stat changes: [Attack, Defense, Sp. Atk, Sp. Def, Spe, Crit]
    let getbst;
    if (this.move[3] === "P") {
      getbst = [1, 2];
    } else if (this.move[3] === "S") {
      getbst = [3, 4];
    } else {
      getbst = null;
    }

    if (this.move[3] !== "N") {
      let stab = 1;
      let crit = 1;
      let item = 1;
      let selfchnew = null;
      let enemychnew = null;
      if (this.move[1] === this.type) {
        stab *= 1.5;
      }
      if (Math.round(Math.random() * 16) >= 16 / selfch[5]) {
        crit *= 1.5;
        if (selfch[getbst[0] - 1] < 1) {
          selfchnew = 1;
        }
        if (enemych[getbst[0] - 1] > 1) {
          enemychnew = 1;
        }
      }
      const multi = stab * typeChart[this.move[1]][enemy.type] * crit * item;
      let attack, defense, powerBonus, damage;
      if (selfchnew !== null || enemychnew !== null) {
        attack = (((this.bst[getbst[0]] * 2 + 31 + 252 / 4) * this.level) / 100 + 5) * (selfchnew || selfch[0]);
        defense = (((enemy.bst[getbst[1]] * 2 + 31 + 252 / 4) * enemy.level) / 100 + 5) * (enemychnew || enemych[1]);
        powerBonus = [10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 50][Math.floor(Math.random() * 11)];
        damage = (((2 * this.level) / 250) * attack / defense * (this.move[2] + powerBonus) + 2) * multi;
      } else {
        attack = (((this.bst[getbst[0]] * 2 + 31 + 252 / 4) * this.level) / 100 + 5) * selfch[0];
        defense = (((enemy.bst[getbst[1]] * 2 + 31 + 252 / 4) * enemy.level) / 100 + 5) * enemych[1];
        powerBonus = [10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 50][Math.floor(Math.random() * 11)];
        damage = (((2 * this.level) / 250) * attack / defense * (this.move[2] + powerBonus) + 2) * multi;
      }
      return damage;
    }
  }
}

