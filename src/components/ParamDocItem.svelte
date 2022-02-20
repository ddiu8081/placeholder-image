<script lang="ts">
  export let serverName: string
  export let config: {
    title: string
    desc: string
    param?: string[]
    eg?: string[]
  }
</script>

<section class="mt-6 mb-8">
  <h3 class="text-lg font-semibold">{config.title}</h3>
  <p class="mt-2 opacity-50 text-sm">{config.desc}</p>
  {#if (config.param)}
    {#each config.param as paramItem}
      <div class="mt-2 text-sm font-mono text-teal-600 break-words">
        {serverName}/{paramItem}
      </div>
    {/each}
  {/if}
  {#if (config.eg)}
    <p class="mt-3 opacity-50 text-sm">Examples:</p>
    {#each config.eg as egItem}
      <img src="{serverName}/{egItem}" alt="example" class="mt-2">
      <a href="{serverName}/{egItem}" target="_blank" class="mt-2 text-xs font-mono text-teal-600 break-words">
        {serverName}/{egItem}
      </a>
    {/each}
  {/if}
</section>