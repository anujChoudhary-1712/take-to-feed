export const THEMES = {
  episode: ['Give every edit note a home', '#d9f0dd'],
  assignment: ['Assign the exact cut', '#f1dfa6'],
  resolved: ['Close the loop', '#d9f0dd'],
};

export function groupCaptions(words) {
  const groups = [];
  let phrase = [];
  for (const word of words) {
    phrase.push(word);
    if (phrase.length === 12 || /[.!?]$/.test(word.text.trim()) || word === words.at(-1)) {
      groups.push({
        startMs: phrase[0].startMs,
        endMs: phrase.at(-1).endMs,
        text: phrase.map((part) => part.text.trim()).join(' '),
      });
      phrase = [];
    }
  }
  return groups;
}

export function beatFor(cut) {
  return cut.media.split('/').at(-1).replace(/\.m4a$/, '');
}
