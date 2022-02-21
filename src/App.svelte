<script lang="ts">
  import Icon from '@iconify/svelte'

  import ParamDocItem from './components/ParamDocItem.svelte'
  import Credits from './components/Credits.svelte'

  const serverName = 'https://img.ph.ljl.li'
  const params = '{size}/{background?}/{foreground?}{ext?}?text={text?}'

  const configs = [
    {
      title: 'Image Size (Required)',
      desc: 'Specify width and height. If only one value is specified, it will be used for both width and height.',
      param: [
        '[width]x[height]',
        '[width]',
      ],
      eg: [
        '240x80',
      ],
    }, {
      title: 'Custom Color',
      desc: 'Specify custom background color or foreground color.',
      param: [
        '[background]/[foreground]',
        '[background]',
      ],
      eg: [
        '240x80/ffedd5',
        '240x80/06b6d4/ffffff',
      ],
    }, {
      title: 'Custom Text',
      desc: 'Coming soon.',
    }, {
      title: 'Image Format',
      desc: 'Coming soon.',
    }, {
      title: 'Professional mode',
      desc: 'Coming soon.',
    },
  ]
</script>

<main>
  <div class="container max-w-prose mx-auto mt-16 mb-10 px-6 md:px-0">
    <header class="py-2">
      <Icon class="text-6xl" icon="twemoji:ice" />
      <h1 class="text-3xl font-semibold mt-6">Placeholder Image</h1>
      <p class="opacity-50 mt-2">Generate placeholder images by simply adding params.</p>
    </header>
    <img class="mt-4 rounded-lg w-full" src="//img.ph.ljl.li/720x240" alt="banner">
    <article>
      <div class="my-12">
        <h2 class="uppercase opacity-50 text-sm">How To Use</h2>
        <div
          class="px-4 py-3 mx-0 my-3 break-words bg-blue-gray-100 border border-blue-gray-200 rounded-lg"
        >
          <span class="text-md font-semibold font-mono text-gray-600">{serverName}/{params}</span>
        </div>
      </div>
      <div class="my-12">
        <h2 class="uppercase opacity-50 text-sm">Params</h2>
        {#each configs as item (item.title)}
          <ParamDocItem {serverName} config={item} />
        {/each}
      </div>
      <Credits />
    </article>
    <footer class="text-sm opacity-50 py-4">
      Made by
      <a href="https://ljl.li/">Diu</a>
       | 
       <a href="https://github.com/ddiu8081/placeholder-image">Source Code</a>
    </footer>
  </div>
</main>
