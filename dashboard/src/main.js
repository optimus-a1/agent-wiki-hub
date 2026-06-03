async function loadJson(path) {
  const response = await fetch(path);
  return response.json();
}

async function render() {
  const summary = await loadJson('data/dashboard-summary.json');
  const packs = await loadJson('data/packs.json');
  document.getElementById('summary').innerHTML = `
    <div class="grid">
      <article><span>Wikis</span><strong>${summary.wiki_count}</strong></article>
      <article><span>Pages</span><strong>${summary.page_count}</strong></article>
      <article><span>Acceptance</span><strong>${summary.acceptance_passed ? 'PASS' : 'OPEN'}</strong></article>
      <article><span>Open Topics</span><strong>${summary.open_source_topics}</strong></article>
      <article><span>Verified Tickets</span><strong>${summary.verified_tickets}</strong></article>
      <article><span>Current Fact Ready</span><strong>${summary.current_fact_ready ? 'yes' : 'no'}</strong></article>
    </div>`;
  document.getElementById('packs').innerHTML = packs.packs.map((pack) => `<li>${pack}</li>`).join('');
}

render().catch((error) => {
  document.getElementById('summary').textContent = `Unable to load dashboard data: ${error.message}`;
});
