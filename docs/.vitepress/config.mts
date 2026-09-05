import { defineConfig, type DefaultTheme } from 'vitepress'

// Curriculum phases in learning order. Lessons listed here appear in the sidebar;
// add a lesson to `lessons` when its page exists under docs/curriculum/<slug>/.
const phases: { num: string; slug: string; title: string; lessons?: { text: string; file: string }[] }[] = [
  {
    num: '00',
    slug: '00-orientation',
    title: 'Orientation',
    lessons: [
      { text: 'Day 1 — What Is AI?', file: '01-what-is-ai' },
      { text: 'Day 2 — Set Up Your Environment', file: '02-environment-setup' },
    ],
  },
  { num: '01', slug: '01-python', title: 'Python for AI/DevOps' },
  { num: '02', slug: '02-ai-fundamentals', title: 'AI Fundamentals' },
  { num: '03', slug: '03-math-for-ai', title: 'Math for AI' },
  { num: '04', slug: '04-machine-learning', title: 'Machine Learning' },
  { num: '05', slug: '05-deep-learning', title: 'Deep Learning' },
  { num: '06', slug: '06-transformers', title: 'Transformers' },
  { num: '07', slug: '07-llm-engineering', title: 'LLM Engineering' },
  { num: '08', slug: '08-rag', title: 'RAG' },
  { num: '09', slug: '09-ai-agents', title: 'AI Agents' },
  { num: '10', slug: '10-mlops', title: 'MLOps' },
  { num: '11', slug: '11-llmops', title: 'LLMOps' },
  { num: '12', slug: '12-ai-observability', title: 'AI Observability' },
  { num: '13', slug: '13-gpu-infrastructure', title: 'GPU Infrastructure' },
  { num: '14', slug: '14-ai-kubernetes', title: 'AI + Kubernetes' },
  { num: '15', slug: '15-ai-security', title: 'AI Security' },
  { num: '16', slug: '16-ai-cost-engineering', title: 'AI Cost Engineering' },
  { num: '17', slug: '17-capstone-ai-sre', title: 'AI-SRE Capstone' },
]

const curriculumSidebar: DefaultTheme.SidebarItem[] = [
  { text: 'Curriculum overview', link: '/curriculum/' },
  ...phases.map((p) => ({
    text: `${p.num} · ${p.title}`,
    collapsed: p.num !== '00',
    items: [
      { text: 'Phase overview', link: `/curriculum/${p.slug}/` },
      ...(p.lessons ?? []).map((l) => ({ text: l.text, link: `/curriculum/${p.slug}/${l.file}` })),
    ],
  })),
]

export default defineConfig({
  title: 'AI for DevOps',
  description:
    'A production-oriented curriculum taking a DevOps engineer from zero AI knowledge to AI Platform Engineer.',
  lang: 'en-US',
  lastUpdated: true,
  cleanUrls: true,
  // If deploying to GitHub Pages under a project path, set base to '/ai-devops/'.
  // base: '/ai-devops/',

  themeConfig: {
    siteTitle: 'AI for DevOps',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Roadmap', link: '/roadmap' },
      { text: 'Progress', link: '/progress' },
      { text: 'Curriculum', link: '/curriculum/' },
      { text: 'Labs', link: '/labs/' },
      { text: 'Projects', link: '/projects/' },
      { text: 'Interview Prep', link: '/interview-prep/' },
      { text: 'Resources', link: '/resources' },
    ],

    sidebar: {
      '/curriculum/': curriculumSidebar,
      '/labs/': [
        { text: 'Labs', link: '/labs/' },
        { text: 'Curriculum', link: '/curriculum/' },
      ],
      '/projects/': [
        { text: 'Projects', link: '/projects/' },
        { text: 'Curriculum', link: '/curriculum/' },
      ],
      '/interview-prep/': [
        { text: 'Interview Prep', link: '/interview-prep/' },
        { text: 'Curriculum', link: '/curriculum/' },
      ],
    },

    outline: { level: [2, 3], label: 'On this page' },

    socialLinks: [{ icon: 'github', link: 'https://github.com/rairamjee/ai-devops' }],

    editLink: {
      pattern: 'https://github.com/rairamjee/ai-devops/edit/main/docs/:path',
      text: 'Edit this page on GitHub',
    },

    search: { provider: 'local' },

    footer: {
      message: 'DevOps first. AI second. Production always.',
    },
  },
})
