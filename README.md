# Análisis DNP-Sectores
# Análisis DNP-Sectores

<h1>Análisis de inversiones en Sectores del País según DNP </h1>

<h2>Introducción</h2> <br>
<p>En base a datos recopilados del Departamento Nacional de Planeación, se ha obtenido información relevante para realizar un análisis de la inversión en diversos sectores clave, como educación, interior, salud, cultura e inclusión social, entre otros. El objetivo principal de este análisis es comprender de manera más precisa la distribución de los recursos de inversión a nivel territorial, implementada por las distintas entidades gubernamentales.</p> <br>

<h2>Objetivos</h2> <br>

<h3>General</h3> <br>
<p>Evaluar los sectores mediante el marco de desempeño de inversión en diferentes sectores de Colombia, empleando visualizaciones.</p>

<h3>Específicos</h3> <br>
<ol>
  <li>Visualizar datos generales de todos los sectores</li>
  <li>Seleccionar los sectores que tienen mayor importancia en el desarrollo productivo y equitativo del país</li>
  <li>Comparar los datos obtenidos con otras fuentes a disposición del público</li>
</ol> <br>

<h2>Manual de Clasificación de la Inversión Pública</h2>

<p>El Manual de Clasificación de la Inversión Pública es una herramienta que proporciona las definiciones y lineamientos necesarios para la clasificación de los sectores, así como para la formulación de programas, subprogramas y proyectos de inversión. Este manual está dirigido por el artículo 2.2.6.2.1. del Decreto 1082 de 2015 y tiene como objetivos principales:</p>

<ol>
  <li>Facilitar y orientar la formulación de los programas, subprogramas y proyectos de inversión.</li>
  <li>Orientar las decisiones de gobierno en todos sus niveles (nación y territorio), los Órganos Autónomos y el Congreso de la República sobre qué se quiere lograr con los recursos públicos.</li>
  <li>Avanzar hacia la consolidación de un Presupuesto Orientado a Resultados.</li>
  <li>Propender por una correcta articulación entre planeación, presupuestación y ejecución del gasto.</li>
  <li>Garantizar una adecuada comprensión y análisis del presupuesto por parte de la ciudadanía (Manual de clasificación presupuestal, 2017).</li>
</ol>

<p>Para comprender la ubicación de un sector dentro de la clasificación, se hace necesario entender las definiciones del marco de clasificación, que se divide en los siguientes niveles:</p>

<h3>Sección</h3>
<p>La sección es la identidad responsable y ejecutora de los recursos. Representa una agrupación de sectores afines y tiene a su cargo la gestión de programas y proyectos relacionados.</p>

<h3>Programa</h3>
<p>El programa es el nivel encargado de coordinar los proyectos de inversión y actividades mediante la intervención del gobierno. Establece metas para la obtención de resultados y busca generar impacto en la sociedad.</p>

<h3>Subprograma</h3>
<p>El subprograma es una subdivisión del programa que se evalúa en el Task1_DatasetProject. Está compuesto por un plan estratégico que incluye una serie de proyectos específicos que trabajan juntos para lograr objetivos a largo plazo en un campo particular.</p>

<h3>Proyecto</h3>
<p>El proyecto corresponde a los proyectos de inversión pública, los cuales tienen como objetivo mejorar, crear o recuperar la capacidad de producción de bienes y servicios por parte del Estado.</p>

<p>A través de la clasificación de la inversión pública en estos niveles, se busca promover la eficiencia en la asignación de recursos y asegurar que se alcancen los resultados esperados en términos de beneficios para la sociedad.(Manual de clasificación presupuestal (2017))</p>

<p>Las inversiones públicas se clasifican en: </p>

<pre>
<code>
array(['Interior', 'Inclusión Social Y Reconciliación',
       'Agricultura Y Desarrollo Rural', 'Cultura', 'Educación',
       'Deporte Y Recreación', 'Ambiente Y Desarrollo Sostenible',
       'Transporte', 'Vivienda Ciudad Y Territorio',
       'Gobierno Territorial', 'Salud Y Protección Social',
       'Ciencia Tecnología E Innovación', 'Planeación', 'Minas Y Energía',
       'Trabajo', 'Comercio Industria Y Turismo',
       'Presidencia De La República', 'Empleo Público',
       'Justicia Y Del Derecho', 'Información Estadística', 'Hacienda',
       'Tecnologías De La Información Y Las Comunicaciones',
       'Organismos De Control', 'Fiscalía', 'Rama Judicial',
       'Registraduría', 'Congreso De La República',
       'Relaciones Exteriores',
       'Sistema Integral De Verdad Justicia Reparación Y No Repetición'],
      dtype=object)
</code>
</pre>
<br>
<p>La evaluación por sector nos brinda una visión clara de cómo se distribuye la inversión, revelando cuáles sectores han recibido un mayor flujo de recursos y cuáles han experimentado una menor asignación financiera. Este análisis nos permite identificar las áreas de mayor interés y enfoque para la inversión pública, así como aquellas que podrían requerir una mayor atención y apoyo. Al comprender esta distribución de la inversión, podemos tomar decisiones informadas y estratégicas para maximizar el impacto de los recursos y garantizar un desarrollo equitativo y sostenible en todos los sectores involucrados.</p>

<img src="https://github.com/MayelinAguilar/Task1_DatasetProject/blob/main/Figure_1.png" alt="Inversión por sectores">

<p>Según los indicadores reflejados, se evidencia una mayor inversión en el sector de Transporte. Estos datos demuestran un crecimiento significativo en los recursos destinados a esta área, lo cual indica su relevancia y potencial en el panorama económico actual. La inversión en infraestructura, sin embargo existe poco desarrollo y modernización en el sistema de transporte ya que las redes viales son algunos de los aspectos clave en los que se ha enfocado esta inversión. Se espera que la visión cambie de enfoque estratégico en el sector de Transporte para mejorar la conectividad, la movilidad de bienes y personas, y promover un desarrollo sostenible en la industria. </p> <br>

<p>Aqui se puede reflejar el promedio de ingresos:</p> <br>

<pre>
<code>
Transporte                                                        44369
Inclusión Social Y Reconciliación                                 37277
Salud Y Protección Social                                         35557
Vivienda Ciudad Y Territorio                                      35329
Educación                                                         35243
Gobierno Territorial                                              28358
Agricultura Y Desarrollo Rural                                    23933
Ambiente Y Desarrollo Sostenible                                  21367
Deporte Y Recreación                                              20572
Cultura                                                           19035
Ciencia Tecnología E Innovación                                   10780
Minas Y Energía                                                    9913
Comercio Industria Y Turismo                                       9808
Planeación                                                         6813
Justicia Y Del Derecho                                             6324
Tecnologías De La Información Y Las Comunicaciones                 5478
Trabajo                                                            5440
Interior                                                           5098
Información Estadística                                            2341
Hacienda                                                           2294
Presidencia De La República                                        2146
Empleo Público                                                     1973
Organismos De Control                                              1174
Fiscalía                                                            414
Relaciones Exteriores                                               329
Rama Judicial                                                       267
Registraduría                                                       196
Congreso De La República                                            115
Sistema Integral De Verdad Justicia Reparación Y No Repetición       88
</code>
</pre>

<p>Se realiza un análisis exhaustivo para compararlo con otros sectores que influyen en la estabilidad económica de un país, compararlo </p> <br>

<ol>
  <li>Transporte</li>
  <li>Educación</li>
  <li>Inclusión social y reconciliación</li>
  <li>Educación</li>
  <li>Ciencia y Tecnología e Innovación</li>
  <li>Trabajo</li>
  <li>Empleo públicon</li>
</ol> <br>

<img src="https://github.com/MayelinAguilar/Task1_DatasetProject/blob/main/Sectores%20Escogidos.png?raw=true" alt="Inversión por sectores">

<p>Según el análisis de la gráfica, se observa una menor inversión en los sectores de innovación tecnológica, trabajo y empleo público. Estos hallazgos destacan la importancia estratégica de estos sectores en el desarrollo de un país y revelan la existencia de desigualdades que afectan a los ciudadanos colombianos, generando una falta de oportunidades significativa. Es fundamental abordar estas disparidades y promover políticas que impulsen el crecimiento equitativo y la creación de empleo en dichos sectores para fomentar un desarrollo sostenible y brindar mejores perspectivas a la población. </p> <br>

<p>A continuación se puede ver cuantas veces se ha invertido en estos sectores flutuan en el gráfico de Avance de indicador, donde hay mayor concentración y que se espera por lo menos para el siguiente año como sería su comportamiento, en temas de avance de desarrollo. </p> <br>

<img src="https://github.com/MayelinAguilar/Task1_DatasetProject/blob/main/dispersion.png?raw=true" alt="Dispersión">

<p>Para comprender su comportamiento, se puede utilizar esta regresión lineal como una representación de las inversiones realizadas en Colombia a lo largo del tiempo.</p> <br>

<img src="https://github.com/MayelinAguilar/Task1_DatasetProject/blob/main/linealizacion.png?raw=true" alt="Tendencia Lineal">

<p>A través del análisis de los datos, se puede apreciar claramente una tendencia decreciente en la inversión destinada al sistema integral de verdad, justicia, reparación y no repetición en Colombia. Este fenómeno puede ser atribuido a los complejos conflictos geopolíticos que han impactado al país en los últimos años. Estas circunstancias han generado desafíos significativos para la implementación y financiamiento de programas orientados a la reconciliación y la justicia, afectando así la asignación de recursos en este importante sector. Es fundamental abordar estos desafíos para promover una paz sostenible y garantizar la construcción de un futuro más equitativo y reconciliado en Colombia.</p> <br>

<p>Realizando una proyección sobre cómo se comportaría el nivel de frecuencia de inversión, se pueden identificar oportunidades para mejorar la inversión en sectores como Trabajo e Innovación tecnológica. A través de un análisis detallado, se pueden identificar áreas clave donde se podría enfocar la inversión para impulsar el crecimiento y el desarrollo en estos sectores. Es crucial explorar estrategias innovadoras y políticas efectivas que fomenten la creación de empleo, promuevan la investigación y el desarrollo tecnológico, y estimulen la colaboración entre el sector público y privado. Estas acciones pueden conducir a un mayor impulso económico y a la generación de oportunidades que beneficien tanto a la sociedad como a la competitividad del país.</p> <br>

<img src="https://github.com/MayelinAguilar/Task1_DatasetProject/blob/main/linealizacion.png?raw=true" alt="linealizacion">

<h2>Bibliografia</h2> <br>

<p>
Por último, al hacer una proyección de futuras inversiones, se vislumbra que el sector transporte continuará siendo una prioridad destacada. Además, se prevé un crecimiento significativo en el sector de Educación. Sin embargo, es importante destacar que el sector trabajo presenta un aumento modesto, ya que muchas personas aún se enfrentan a limitaciones en recursos y la visión empresarial y tecnológica en Colombia aún muestra brechas significativas. Es fundamental abordar estas limitaciones y promover un enfoque más sólido en la creación de empresas y la adopción de nuevas tecnologías, para impulsar un desarrollo económico más inclusivo y sostenible en el país.</p> 

<p>DNP (Mayo 2018), Dirección de Inversiones y Finanzas Públicas, Subdirección de Proyectos e Información para la Inversión Pública. Manual de Clasificación de la Inversión Pública (Versión 5).Recuperado de: https://colaboracion.dnp.gov.co/CDT/Inversiones%20y%20finanzas%20pblicas/MGA_WEB/Manual%20clasificaci%C3%B3n%20de%20la%20inversi%C3%B3n%20V%205.0.pdf </p> <br>

<p>DNP (Febrero 2023),Mamnual de clasificación progrmático del gasto Público. Dirección de Proyectos e Información para la Inversión Pública. (Versión 6.7).Recuperado de: https://mgaayuda.dnp.gov.co/Recursos/Manual_de_clasificacion_programatico.pdf </p> <br>
