<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>TAAO-TAPA | Auditoría Judicial de IA</title>
<style>
  * { box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }
  body { background: linear-gradient(135deg, #1e3c72, #2a5298); margin: 0; padding: 20px; color: #333; }
  .container { max-width: 1200px; margin: auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }
  h1 { color: #1e3c72; text-align: center; border-bottom: 3px solid #d4af37; padding-bottom: 10px; }
  h2 { color: #2a5298; border-left: 5px solid #d4af37; padding-left: 10px; }
  h3 { color: #1e3c72; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0; }
  .panel { background: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #dee2e6; }
  .slider-group { margin: 15px 0; }
  .slider-group label { display: block; font-weight: bold; margin-bottom: 5px; color: #2a5298; }
  .slider-group input[type=range] { width: 100%; }
  .slider-value { display: inline-block; background: #1e3c72; color: white; padding: 2px 10px; border-radius: 15px; font-weight: bold; margin-left: 10px; }
  button { background: linear-gradient(135deg, #d4af37, #b8941f); color: white; border: none; padding: 15px 30px; font-size: 18px; font-weight: bold; border-radius: 10px; cursor: pointer; width: 100%; margin-top: 20px; transition: transform 0.2s; }
  button:hover { transform: scale(1.02); }
  .results { margin-top: 30px; display: none; }
  .metrics { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin: 20px 0; }
  .metric { background: #fff; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-top: 4px solid #1e3c72; }
  .metric-value { font-size: 32px; font-weight: bold; color: #1e3c72; }
  .metric-label { font-size: 14px; color: #666; }
  .risk-box { padding: 20px; border-radius: 10px; margin: 15px 0; font-size: 20px; font-weight: bold; text-align: center; }
  .risk-stable { background: #d4edda; color: #155724; border: 2px solid #28a745; }
  .risk-low { background: #fff3cd; color: #856404; border: 2px solid #ffc107; }
  .risk-medium { background: #ffe5d0; color: #984a15; border: 2px solid #fd7e14; }
  .risk-high { background: #f8d7da; color: #721c24; border: 2px solid #dc3545; }
  .risk-critical { background: #343a40; color: #fff; border: 2px solid #000; }
  .alert { background: #fff3cd; border-left: 5px solid #ffc107; padding: 12px; margin: 10px 0; border-radius: 5px; }
  .info { background: #d1ecf1; border-left: 5px solid #17a2b8; padding: 12px; margin: 10px 0; border-radius: 5px; }
  .hash-box { background: #212529; color: #28a745; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; word-break: break-all; font-size: 12px; }
  .sidebar { background: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 20px; }
  .sidebar input, .sidebar select { width: 100%; padding: 8px; margin: 5px 0; border: 1px solid #ced4da; border-radius: 5px; }
</style>
</head>
<body>
<div class="container">
  <h1>⚖️ TAAO–TAPA: Sistema de Auditoría de IA Judicial</h1>
  <p style="text-align:center; color:#666;">Prototipo de Tesis Doctoral | Dr. Edgar Zabaleta | Caracas, Venezuela</p>

  <div class="sidebar">
    <h3>👤 Datos del Operador</h3>
    <label>Rol Judicial:</label>
    <select id="userRole">
      <option>Juez</option><option>Fiscal</option><option>Defensor</option><option>Perito</option><option>Administrador</option>
    </select>
    <label>ID del Caso / Expediente:</label>
    <input type="text" id="caseId" value="EXP-2026-001">
  </div>

  <h2>📊 Evaluación de Variables (Escala 0 a 10)</h2>
  <div class="grid">
    <div class="panel">
      <h3>🔍 Variables TAAO (Trazabilidad y Control)</h3>
      <div class="slider-group"><label>T1. Trazabilidad <span class="slider-value" id="T1v">5.0</span></label><input type="range" id="T1" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('T1v').textContent=this.value"></div>
      <div class="slider-group"><label>T2. Transparencia <span class="slider-value" id="T2v">5.0</span></label><input type="range" id="T2" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('T2v').textContent=this.value"></div>
      <div class="slider-group"><label>T3. Explicabilidad <span class="slider-value" id="T3v">5.0</span></label><input type="range" id="T3" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('T3v').textContent=this.value"></div>
      <div class="slider-group"><label>T4. Auditabilidad <span class="slider-value" id="T4v">5.0</span></label><input type="range" id="T4" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('T4v').textContent=this.value"></div>
      <div class="slider-group"><label>T5. Supervisión Humana <span class="slider-value" id="T5v">5.0</span></label><input type="range" id="T5" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('T5v').textContent=this.value"></div>
    </div>
    <div class="panel">
      <h3>⚠️ Variables TAPA (Riesgos y Patologías)</h3>
      <div class="slider-group"><label>P1. Nivel de Sesgo <span class="slider-value" id="P1v">5.0</span></label><input type="range" id="P1" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('P1v').textContent=this.value"></div>
      <div class="slider-group"><label>P2. Riesgo Jurídico <span class="slider-value" id="P2v">5.0</span></label><input type="range" id="P2" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('P2v').textContent=this.value"></div>
      <div class="slider-group"><label>P3. Impacto Constitucional <span class="slider-value" id="P3v">5.0</span></label><input type="range" id="P3" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('P3v').textContent=this.value"></div>
      <div class="slider-group"><label>P4. Potencial de Discriminación <span class="slider-value" id="P4v">5.0</span></label><input type="range" id="P4" min="0" max="10" step="0.5" value="5" oninput="document.getElementById('P4v').textContent=this.value"></div>
    </div>
  </div>

  <button onclick="ejecutarAuditoria()">🔍 EJECUTAR AUDITORÍA JURÍDICO-ALGORÍTMICA</button>

  <div class="results" id="results">
    <h2>📈 Resultados Técnicos</h2>
    <div class="metrics">
      <div class="metric"><div class="metric-value" id="ita">-</div><div class="metric-label">ITA<br>(Trazabilidad)</div></div>
      <div class="metric"><div class="metric-value" id="irj">-</div><div class="metric-label">IRJ<br>(Riesgo Jurídico)</div></div>
      <div class="metric"><div class="metric-value" id="iia">-</div><div class="metric-label">IIA<br>(Impacto Algorítmico)</div></div>
      <div class="metric"><div class="metric-value" id="igga">-</div><div class="metric-label">IGGA<br>(Índice Global)</div></div>
    </div>

    <h2>🏛️ Clasificación Jurídica</h2>
    <div id="riskBox" class="risk-box"></div>

    <h2>📜 Análisis Jurisprudencial y Constitucional</h2>
    <div id="alertsContainer"></div>

    <h2>🔐 Trazabilidad Inmutable</h2>
    <div class="hash-box" id="hashBox"></div>
  </div>
</div>

<script>
// Función SHA-256 simple
async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

async function ejecutarAuditoria() {
  const T1 = parseFloat(document.getElementById('T1').value);
  const T2 = parseFloat(document.getElementById('T2').value);
  const T3 = parseFloat(document.getElementById('T3').value);
  const T4 = parseFloat(document.getElementById('T4').value);
  const T5 = parseFloat(document.getElementById('T5').value);
  const P1 = parseFloat(document.getElementById('P1').value);
  const P2 = parseFloat(document.getElementById('P2').value);
  const P3 = parseFloat(document.getElementById('P3').value);
  const P4 = parseFloat(document.getElementById('P4').value);

  // Fórmulas TAAO
  const ita = (0.25*T1 + 0.20*T2 + 0.20*T3 + 0.20*T4 + 0.15*T5).toFixed(2);
  const irj = (0.35*P1 + 0.30*P2 + 0.25*P3 + 0.10*P4).toFixed(2);
  const iia = ((10-T2) * (10-T1)).toFixed(2);
  const igga = (0.70*ita - 0.23*irj + 0.07*iia).toFixed(2);

  document.getElementById('ita').textContent = ita;
  document.getElementById('irj').textContent = irj;
  document.getElementById('iia').textContent = iia;
  document.getElementById('igga').textContent = igga;

  // Motor Jurídico-Jurisprudencial
  const alerts = [];
  const legalFlags = [];
  const constAnalysis = [];

  if (T3 < 4 || P1 > 7) { alerts.push("⚠️ Posible afectación del debido proceso por baja explicabilidad (T3<4) o sesgo elevado (P1>7)."); legalFlags.push("DUE_PROCESS_RISK"); }
  if (T2 < 5 && T4 < 5) { alerts.push("⚠️ Riesgo de falta de motivación del acto automatizado (Transparencia y Auditabilidad bajas)."); legalFlags.push("MOTIVATION_RISK"); }
  if (P4 > 6) { alerts.push("⚠️ Posible discriminación algorítmica indirecta detectada (P4>6)."); legalFlags.push("DISCRIMINATION_RISK"); }
  if (T1 < 5 || T2 < 5) { alerts.push("⚠️ Baja transparencia afecta el control judicial."); legalFlags.push("TRANSPARENCY_RISK"); }

  if (P1 > 6) constAnalysis.push("📜 Posible vulneración del principio de igualdad ante la ley (Art. 21 CRBV).");
  if (T3 < 4) constAnalysis.push("📜 Déficit de explicabilidad afecta el derecho a la defensa (Art. 49 CRBV).");
  if (T4 < 4) constAnalysis.push("📜 Baja auditabilidad compromete el control jurisdiccional y la tutela judicial efectiva.");

  // Clasificación
  const score = legalFlags.length;
  let riskLevel, riskClass;
  if (score === 0) { riskLevel = "✅ JURÍDICAMENTE ESTABLE"; riskClass = "risk-stable"; }
  else if (score === 1) { riskLevel = "⚠️ RIESGO LEGAL BAJO"; riskClass = "risk-low"; }
  else if (score === 2) { riskLevel = "🚨 RIESGO LEGAL MEDIO"; riskClass = "risk-medium"; }
  else if (score === 3) { riskLevel = "🛑 RIESGO LEGAL ALTO"; riskClass = "risk-high"; }
  else { riskLevel = "💀 RIESGO LEGAL CRÍTICO (INAPLICABLE)"; riskClass = "risk-critical"; }

  const riskBox = document.getElementById('riskBox');
  riskBox.textContent = riskLevel;
  riskBox.className = "risk-box " + riskClass;

  // Mostrar alertas
  const alertsContainer = document.getElementById('alertsContainer');
  alertsContainer.innerHTML = '';
  if (alerts.length === 0) {
    alertsContainer.innerHTML = '<div class="info">✅ No se detectaron alertas jurisprudenciales críticas. El sistema cumple con los estándares.</div>';
  } else {
    alerts.forEach(a => { const div = document.createElement('div'); div.className = 'alert'; div.textContent = a; alertsContainer.appendChild(div); });
  }
  constAnalysis.forEach(c => { const div = document.createElement('div'); div.className = 'info'; div.textContent = c; alertsContainer.appendChild(div); });

  // Hash inmutable
  const userRole = document.getElementById('userRole').value;
  const caseId = document.getElementById('caseId').value;
  const timestamp = new Date().toISOString();
  const rawString = `${userRole}:${caseId}:EVALUATION:ITA:${ita}:IRJ:${irj}:IIA:${iia}:IGGA:${igga}:${timestamp}`;
  const hash = await sha256(rawString);
  document.getElementById('hashBox').innerHTML = `<strong>Hash SHA-256 (Trazabilidad Inmutable):</strong><br>${hash}<br><br><small>Timestamp: ${timestamp}<br>Este hash garantiza que la evaluación no ha sido alterada (Res. TSJ 2025-006).</small>`;

  document.getElementById('results').style.display = 'block';
  document.getElementById('results').scrollIntoView({behavior: 'smooth'});
}
</script>
</body>
</html>
