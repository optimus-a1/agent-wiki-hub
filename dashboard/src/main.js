async function loadJson(path) {
  const response = await fetch(path);
  return response.json();
}

async function render() {
  const summary = await loadJson('data/dashboard-summary.json');
  const packs = await loadJson('data/packs.json');
  const density = await loadJson('data/knowledge-density.json');
  const highRisk = await loadJson('data/high-risk-boundaries.json');
  const currentFact = await loadJson('data/current-fact-gates.json');
  const mocStatus = await loadJson('data/wiki-moc-status.json');
  document.getElementById('summary').innerHTML = `
    <div class="grid">
      <article><span>Wikis</span><strong>${summary.wiki_count}</strong></article>
      <article><span>Pages</span><strong>${summary.page_count}</strong></article>
      <article><span>Acceptance</span><strong>${summary.acceptance_passed ? 'PASS' : 'OPEN'}</strong></article>
      <article><span>Open Topics</span><strong>${summary.open_source_topics}</strong></article>
      <article><span>Verified Tickets</span><strong>${summary.verified_tickets}</strong></article>
      <article><span>Current Fact Ready</span><strong>${summary.current_fact_ready ? 'yes' : 'no'}</strong></article>
      <article><span>Generated Pages</span><strong>${summary.automation_generated_pages || 0}</strong></article>
      <article><span>Obsidian MOCs</span><strong>${summary.obsidian_moc_count || 0}</strong></article>
    </div>`;
  const rows = (density.records || []).map((record) => {
    const c = record.counts || {};
    return `<tr><td>${record.wiki}</td><td>${record.knowledge_density_group}</td><td>${c.concepts || 0}</td><td>${c.rules || 0}</td><td>${c.workflows || 0}</td><td>${c.cases || 0}</td><td>${c.prompts || 0}</td><td>${record.eval_tests || 0}</td></tr>`;
  }).join('');
  document.getElementById('knowledge-density').innerHTML = `
    <table><thead><tr><th>Wiki</th><th>Group</th><th>Concepts</th><th>Rules</th><th>Workflows</th><th>Cases</th><th>Prompts</th><th>Evals</th></tr></thead><tbody>${rows}</tbody></table>`;
  document.getElementById('gate-status').innerHTML = `
    <article><span>High Risk Boundaries</span><strong>${highRisk.passed ? 'PASS' : 'OPEN'}</strong></article>
    <article><span>Current Fact Gates</span><strong>${currentFact.passed ? 'PASS' : 'OPEN'}</strong></article>
    <article><span>Current Fact Findings</span><strong>${currentFact.finding_count || 0}</strong></article>
    <article><span>Boundary Warnings</span><strong>${(highRisk.legacy_warnings || []).length}</strong></article>`;
  const mocRows = (mocStatus.records || []).map((record) => {
    const c = record.counts || {};
    return `<tr><td>${record.wiki}</td><td>${record.path}</td><td>${c.concepts || 0}</td><td>${c.rules || 0}</td><td>${c.workflows || 0}</td><td>${c.cases || 0}</td><td>${c.prompts || 0}</td><td>${c.evals || 0}</td></tr>`;
  }).join('');
  document.getElementById('moc-status').innerHTML = `
    <table><thead><tr><th>Wiki</th><th>MOC</th><th>Concepts</th><th>Rules</th><th>Workflows</th><th>Cases</th><th>Prompts</th><th>Evals</th></tr></thead><tbody>${mocRows}</tbody></table>`;
  document.getElementById('packs').innerHTML = packs.packs.map((pack) => `<li>${pack}</li>`).join('');
}

render().catch((error) => {
  document.getElementById('summary').textContent = `Unable to load dashboard data: ${error.message}`;
});
