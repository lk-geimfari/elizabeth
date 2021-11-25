# -*- coding: utf-8 -*-

import re
from ipaddress import IPv4Address, IPv6Address

import pytest
import validators
from mimesis import Internet, data
from mimesis.enums import MimeType, PortRange, TLDType, URLScheme
from mimesis.exceptions import NonEnumerableError

from . import patterns


class TestInternet(object):
    @pytest.fixture
    def net(self):
        return Internet()

    def test_str(self, net):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(net))

    def test_emoji(self, net):
        result = net.emoji()
        assert result in data.EMOJI

    def test_hashtags(self, net):
        result = net.hashtags(quantity=5)
        assert len(result) == 5

        with pytest.raises(ValueError):
            net.hashtags(quantity=0)

        with pytest.raises(ValueError):
            net.hashtags(quantity=-1)

    @pytest.mark.parametrize(
        "subdomains",
        [
            [],
            ["app", "core", "api"],
            ["dev", "prod", "test"],
            ["admin", "smtp", "pop3"],
        ],
    )
    def test_hostname(self, net, subdomains):
        hostname = net.hostname(subdomains=subdomains)
        subdomain, *_ = hostname.split(".", 1)

        if subdomains:
            assert subdomain in subdomains

    @pytest.mark.parametrize(
        "scheme",
        (
            URLScheme.HTTP,
            URLScheme.HTTPS,
            URLScheme.FTP,
            URLScheme.SFTP,
            URLScheme.WS,
            URLScheme.WSS,
        ),
    )
    def test_url(self, net, scheme):
        result = net.url(scheme=scheme)
        assert result.startswith(scheme.value)

    @pytest.mark.parametrize(
        "port",
        (
            PortRange.ALL,
            PortRange.WELL_KNOWN,
            PortRange.EPHEMERAL,
            PortRange.REGISTERED,
        ),
    )
    def test_url_with_port(self, net, port):
        url = net.url(port_range=port)
        port_val = int(url.split(":")[-1].replace("/", ""))
        port_start, port_end = port.value
        assert port_start <= port_val <= port_end

    def test_default(self, net):
        uri = net.uri()
        assert uri.split(":")[0].strip() == "https"

    @pytest.mark.parametrize(
        "scheme, port_range, tld_type, subdomains, query_params_count",
        [
            (
                URLScheme.HTTPS,
                PortRange.WELL_KNOWN,
                TLDType.GTLD,
                ["core", "app", "test", "dev"],
                5,
            ),
        ],
    )
    def test_uri_with_parameters(
        self, net, scheme, port_range, tld_type, subdomains, query_params_count
    ):
        uri = net.uri(
            scheme=scheme,
            port_range=port_range,
            tld_type=tld_type,
            subdomains=subdomains,
            query_params_count=query_params_count,
        )
        assert uri.split(":")[0].strip() == scheme.value
        assert validators.url(uri)

    @pytest.mark.parametrize("length", [4, 6, 8, None])
    def test_query_string(self, net, length):
        query_string = net.query_string(length)
        query_params_count = len(query_string.split("&"))

        if length is None:
            assert 1 <= query_params_count <= 10
        else:
            assert query_params_count == length

    @pytest.mark.parametrize("length", [4, 6, 8, None])
    def test_query_parameters(self, net, length):
        query_dict = net.query_parameters(length)
        query_params_count = len(query_dict)

        if length is None:
            assert 1 <= query_params_count <= 10
        else:
            assert query_params_count == length

    def test_slug(self, net):
        with pytest.raises(ValueError):
            net.slug(parts_count=13)

        with pytest.raises(ValueError):
            net.slug(parts_count=1)

        parts_count = 5
        parts = net.slug(parts_count=parts_count).split("-")
        assert len(parts) == parts_count

    def test_user_agent(self, net):
        result = net.user_agent()
        assert result in data.USER_AGENTS

    def test_image_placeholder(self, net):
        result = net.image_placeholder(width=400, height=300)
        assert result is not None

    @pytest.mark.parametrize(
        "w, h, keywords, writable, res_type",
        [
            (900, 900, ["love", "passion", "death"], False, str),
            (800, 800, {"love", "passion", "death"}, False, str),
            (800, 800, None, False, str),
            # (700, 700, ['love', 'passion', 'death'], True, bytes),
        ],
    )
    def test_stock_image(self, net, w, h, keywords, writable, res_type):
        result = net.stock_image(
            width=w,
            height=h,
            keywords=keywords,
            writable=writable,
        )
        assert isinstance(result, res_type)
        if res_type == str:
            assert re.match(patterns.STOCK_IMAGE, result)
            assert result.endswith("?" + ",".join(keywords or []))

    def test_ip_v4_object(self, net):
        ip = net.ip_v4_object()
        assert ip.version == 4
        assert ip.max_prefixlen == 32
        assert re.match(patterns.IP_V4_REGEX, ip.exploded)
        assert isinstance(ip, IPv4Address)

    def test_ip_v4(
        self,
        net,
    ):
        assert re.match(patterns.IP_V4_REGEX, net.ip_v4())

    @pytest.mark.parametrize(
        "port_range",
        [
            PortRange.ALL,
            PortRange.WELL_KNOWN,
            PortRange.EPHEMERAL,
            PortRange.REGISTERED,
        ],
    )
    def test_ip_v4_with_port(self, net, port_range):
        ip = net.ip_v4_with_port(port_range)
        port = int(ip.split(":")[-1])
        port_start, port_end = port_range.value
        assert port_start <= port <= port_end

    def test_ip_v6_object(self, net):
        ip = net.ip_v6_object()
        assert ip.version == 6
        assert ip.max_prefixlen == 128
        assert re.match(patterns.IP_V6_REGEX, ip.exploded)
        assert isinstance(ip, IPv6Address)

    def test_ip_v6(self, net):
        ip = net.ip_v6()
        assert re.match(patterns.IP_V6_REGEX, ip)

    def test_mac_address(self, net):
        mac = net.mac_address()
        assert re.match(patterns.MAC_ADDRESS_REGEX, mac)

    def test_http_method(self, net):
        result = net.http_method()
        assert result in data.HTTP_METHODS

    @pytest.mark.parametrize(
        "mime_type",
        [
            MimeType.APPLICATION,
            MimeType.AUDIO,
            MimeType.IMAGE,
            MimeType.MESSAGE,
            MimeType.TEXT,
            MimeType.VIDEO,
        ],
    )
    def test_content_type(self, net, mime_type):
        ct = net.content_type(mime_type=mime_type)
        ct = ct.split(":")[1].strip()
        assert ct in data.MIME_TYPES[mime_type.value]

    def test_content_type_wrong_arg(self, net):
        with pytest.raises(NonEnumerableError):
            net.content_type(mime_type="nil")

    def test_http_status_code(self, net):
        result = net.http_status_code()
        assert (int(result) >= 100) and (int(result) <= 511)

    def test_http_status_message(self, net):
        result = net.http_status_message()
        assert result in data.HTTP_STATUS_MSGS

    @pytest.mark.parametrize(
        "domain_type",
        [
            TLDType.CCTLD,
            TLDType.GTLD,
            TLDType.GEOTLD,
            TLDType.UTLD,
            TLDType.STLD,
        ],
    )
    def test_top_level_domain(self, net, domain_type):
        res_a = net.top_level_domain(tld_type=domain_type)
        res_b = net.tld(tld_type=domain_type)
        assert res_a in data.TLD[domain_type.value]
        assert res_b in data.TLD[domain_type.value]

    def test_top_level_domain_unsupported(self, net):
        with pytest.raises(NonEnumerableError):
            net.top_level_domain(tld_type="nil")

    @pytest.mark.parametrize(
        "port_range, excepted",
        [
            (PortRange.ALL, (1, 65535)),
            (PortRange.EPHEMERAL, (49152, 65535)),
            (PortRange.REGISTERED, (1024, 49151)),
        ],
    )
    def test_port(self, net, port_range, excepted):
        result = net.port(port_range=port_range)
        assert (result >= excepted[0]) and (result <= excepted[1])

        with pytest.raises(NonEnumerableError):
            net.port("nil")


class TestSeededInternet(object):
    @pytest.fixture
    def i1(self, seed):
        return Internet(seed=seed)

    @pytest.fixture
    def i2(self, seed):
        return Internet(seed=seed)

    def test_emoji(self, i1, i2):
        assert i1.emoji() == i2.emoji()

    def test_hashtags(self, i1, i2):
        assert i1.hashtags() == i2.hashtags()
        assert i1.hashtags(quantity=7) == i2.hashtags(quantity=7)

    def test_hostname(self, i1, i2):
        assert i1.hostname() == i2.hostname()
        assert i1.hostname(subdomains=["app", "core", "api"]) == i2.hostname(
            subdomains=["app", "core", "api"]
        )

    def test_url(self, i1, i2):
        assert i1.url() == i2.url()
        assert i1.url(tld_type=TLDType.GEOTLD) == i2.url(tld_type=TLDType.GEOTLD)

    def test_user_agent(self, i1, i2):
        assert i1.user_agent() == i2.user_agent()

    def test_image_placeholder(self, i1, i2):
        assert i1.image_placeholder() == i2.image_placeholder()
        assert i1.image_placeholder(width=128, height=128) == i2.image_placeholder(
            width=128, height=128
        )

    def test_ip_v4(self, i1, i2):
        assert i1.ip_v4() == i2.ip_v4()

    def test_ip_v4_with_port(self, i1, i2):
        assert i1.ip_v4_with_port(port_range=PortRange.ALL) == i2.ip_v4_with_port(
            port_range=PortRange.ALL
        )

    def test_ip_v4_object(self, i1, i2):
        assert i1.ip_v4_object() == i2.ip_v4_object()

    def test_ip_v6(self, i1, i2):
        assert i1.ip_v6() == i2.ip_v6()

    def test_slug(self, i1, i2):
        assert i1.slug(parts_count=2) == i2.slug(parts_count=2)

    def test_query_string(self, i1, i2):
        assert i1.query_string(length=2) == i2.query_string(length=2)
        assert i1.query_string(length=None) == i2.query_string(length=None)

    def test_query_parameters(self, i1, i2):
        assert i1.query_parameters(length=2) == i2.query_parameters(length=2)
        assert i1.query_parameters(length=None) == i2.query_parameters(length=None)

    def test_ip_v6_object(self, i1, i2):
        assert i1.ip_v6_object() == i2.ip_v6_object()

    def test_mac_address(self, i1, i2):
        assert i1.mac_address() == i2.mac_address()

    def test_http_method(self, i1, i2):
        assert i1.http_method() == i2.http_method()

    def test_content_type(self, i1, i2):
        assert i1.content_type() == i2.content_type()
        assert i1.content_type(mime_type=MimeType.APPLICATION) == i2.content_type(
            mime_type=MimeType.APPLICATION
        )

    def test_http_status_code(self, i1, i2):
        assert i1.http_status_code() == i2.http_status_code()

    def test_http_status_message(self, i1, i2):
        assert i1.http_status_message() == i2.http_status_message()

    def test_top_level_domain(self, i1, i2):
        assert i1.top_level_domain() == i2.top_level_domain()
        assert i1.top_level_domain(tld_type=TLDType.UTLD) == i2.top_level_domain(
            tld_type=TLDType.UTLD
        )

    def test_port(self, i1, i2):
        assert i1.port() == i2.port()
        assert i1.port(port_range=PortRange.REGISTERED) == i2.port(
            port_range=PortRange.REGISTERED
        )
